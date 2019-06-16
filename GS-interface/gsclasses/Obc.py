
import datetime
import pymongo
from pymongo import MongoClient

import gsclasses.Param
from gsclasses.Param import parameter

class OBC:
    
    def __init__(self, dbname = 'CQT', start_time=None, end_time=None):
        
        self.dbname = dbname
        self.st = start_time
        self.et = end_time
        
        self.client = None
        self.db = None

        self.Ts_conditions = {}
        self.common_conditions = {}
        
        self.params = {}

        self.params['curGSSB1'] = parameter('curGSSB1',y_label="Current (mA)", p_title="GSSB1 current")               
        self.params['curGSSB2'] = parameter('curGSSB2',y_label="Current (mA)", p_title="GSSB2 current")               
        self.params['curflash'] = parameter('curFlash',y_label="Current (mA)", p_title="Flash current")               
        self.params['curPWM'] = parameter('curPWM',y_label="Current (mA)", p_title="PWM current")                              
        self.params['temp_a'] = parameter('temp_a',y_label="Temperature (C)",p_title="OBC temperature A",n_factor=0.1 )  
        self.params['temp_b'] = parameter('temp_b',y_label="Temperature (C)",p_title="OBC temperature B",n_factor=0.1 )  
        self.params['pwrGSSB1'] = parameter('pwrGSSB1', y_label="Enable", p_title="GSSB1 power")               
        self.params['pwrGSSB2'] = parameter('pwrGSSB2', y_label="Enable", p_title="GSSB2 power")
        self.params['pwrflash'] = parameter('pwrFlash', y_label="Enable", p_title="Flash power")
        self.params['pwrPWM'] = parameter('pwrPWM', y_label="Enable", p_title="PWM power")

        #these should go to the context menu
        self.params['swload_count'] = parameter('swload_count')               
        self.params['fs_mounted'] = parameter('fs_mounted')               
        self.params['boot_count'] = parameter('boot_count')               
        self.params['boot_cause'] = parameter('boot_cause')               
        self.params['clock'] = parameter('clock')                             
        
        if self.st is not None:
            self.Ts_conditions['$gte'] = int(self.st)
        else:
            self.Ts_conditions['$gte'] = int(1452160013) #GMT: Thursday, January 7, 2016 9:46:53 AM
        if self.et is not None:
            self.Ts_conditions['$lt'] = int(self.et)
    
    #def __del__(self): 
    #    self.client.close()
        
    def connect (self):
        self.client = MongoClient('localhost',27017)
        self.db = self.client[self.dbname]
    
    
    def close(self):
        self.client.close()
        
    def reload(self):
        if self.db is None:
            self.connect()
        
        
        for key, value in self.params.items():
            value.getdata(self.db,self.Ts_conditions)

            
    def test_load(self):
        for key, value in self.params.items():
            value.get_random(self.db,self.Ts_conditions)

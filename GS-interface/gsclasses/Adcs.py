import datetime
import pymongo
from pymongo import MongoClient

from gsclasses import Param
from gsclasses.Param import parameter


class ADCS:
    
    def __init__(self, dbname = 'CQT', start_time=None, end_time=None):
        
        self.dbname = dbname
        self.st = start_time
        self.et = end_time
        
        self.client = None
        self.db = None

        self.Ts_conditions = {}
        self.common_conditions = {}
        
        self.params = {}
        
        self.params['gyro_0'] =  parameter('gyro',idx=0)
        self.params['gyro_1'] =  parameter('gyro',idx=1)
        self.params['gyro_2'] =  parameter('gyro',idx=2)
        self.params['gyro_trend_0'] =  parameter('gyro_trend',idx=0)
        self.params['gyro_trend_1'] =  parameter('gyro_trend',idx=1)
        self.params['gyro_trend_2'] =  parameter('gyro_trend',idx=2)
        self.params['gyro_temp'] = parameter('gyro_temp')
        self.params['gyro_valid'] = parameter('gyro_valid')
        
        self.params['mag_0'] =  parameter('mag',idx=0)
        self.params['mag_1'] =  parameter('mag',idx=1)
        self.params['mag_2'] =  parameter('mag',idx=2)
        self.params['mag_valid'] = parameter('mag_valid')
        
        self.params['suns_temp_0'] =  parameter('suns',idx=0)
        self.params['suns_temp_1'] =  parameter('suns',idx=1)
        self.params['suns_temp_2'] =  parameter('suns',idx=2)
        self.params['suns_temp_3'] =  parameter('suns',idx=3)
        self.params['suns_temp_4'] =  parameter('suns',idx=4)
        self.params['suns_temp_5'] =  parameter('suns',idx=5)  
        #self.params['mag_valid'] =  parameter('mag_valid') 
        
        self.params['torquer_duty_0'] =  parameter('torquer_duty',idx=0)
        self.params['torquer_duty_1'] =  parameter('torquer_duty',idx=1)
        self.params['torquer_duty_2'] =  parameter('torquer_duty',idx=2)  
        
        self.params['status_mag'] = parameter('status_mag')
        self.params['status_css'] = parameter('status_css')
        self.params['status_gyro'] = parameter('status_gyro')
        self.params['status_bdot'] = parameter('status_bdot')
        self.params['status_run'] = parameter('status_run')
        self.params['looptime'] = parameter('looptime')
        self.params['maxlooptime'] = parameter('maxlooptime')
        self.params['bdot_rate_0'] = parameter('bdot_rate',idx=0)
        self.params['bdot_rate_1'] = parameter('bdot_rate',idx=1)
        self.params['bdot_dmag_0'] =  parameter('bdot_dmag',idx=0)
        self.params['bdot_dmag_1'] =  parameter('bdot_dmag',idx=1)
        self.params['bdot_dmag_2'] =  parameter('bdot_dmag',idx=2)       
        self.params['bdot_detumb'] =  parameter('bdot_detumb')       
              
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

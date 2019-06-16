import datetime
import pymongo
from pymongo import MongoClient

from gsclasses import Param
from gsclasses.Param import parameter



class EPS:
    
    def __init__(self, dbname = 'CQT', start_time=None, end_time=None):
        
        self.dbname = dbname
        self.st = start_time
        self.et = end_time
        
        self.client = None
        self.db = None

        self.Ts_conditions = {}
        self.common_conditions = {}
        
        self.params = {}
        
        self.params['vbatt'] = parameter('vbatt')
        
        self.params['temp_0'] =  parameter('temp',idx=0)
        
        self.params['temp_1'] =  parameter('temp',idx=1)
        self.params['temp_2'] =  parameter('temp',idx=2)
        
        self.params['temp_3'] =  parameter('temp',idx=3)
        
        self.params['temp_4'] =  parameter('temp',idx=4) #battery temperature
        self.params['temp_5'] =  parameter('temp',idx=5)
        
        # Solar power input
        self.params['Vin_0'] = parameter('vboost',idx=0,node=2) #node = 2 by default here
        self.params['Vin_1'] = parameter('vboost',idx=1,node=2)
        self.params['Vin_2'] = parameter('vboost',idx=2,node=2)
        self.params['Cin_0'] = parameter('curin',idx=0,node=2) 
        self.params['Cin_1'] = parameter('curin',idx=1,node=2)
        self.params['Cin_2'] = parameter('curin',idx=2,node=2)     
        
        # Power output
        self.params['V_obc'] = parameter('out_val',idx=0,node=2) 
        self.params['V_radio'] = parameter('out_val',idx=3,node=2)
        self.params['V_payload'] = parameter('out_val',idx=5,node=2)
        self.params['C_obc'] = parameter('curout',idx=0,node=2) 
        self.params['C_radio'] = parameter('curout',idx=3,node=2)
        self.params['C_payload'] = parameter('curout',idx=5,node=2)
        
        
        
        self.params['battmode'] = parameter('battmode') 


        # Watchdog timers and bootcauses
        self.params['wdt_i2c'] = parameter('wdtI2cS') 
        self.params['wdt_GND'] = parameter('wdtGndS')
        self.params['boot_cnt'] = parameter('cntBoot')        
        self.params['cntWdtI2c'] = parameter('cntWdtI2c') 
        self.params['cntwdtGND'] = parameter('cntWdtGnd')
        self.params['cntWdtCsp_0'] = parameter('cntWdtCsp',idx=0)         
        self.params['cntWdtCsp_1'] = parameter('cntWdtCsp',idx=1)         
        self.params['bootCause'] = parameter('bootcause')                 
        
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

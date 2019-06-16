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
        
        self.params['vbatt'] = parameter('vbatt',y_label='Voltage (V)',p_title="Battery Level",n_factor=0.001)
        
        self.params['temp_0'] =  parameter('temp',idx=0,y_label='Temperature (C)',p_title="EPS temperature T0")
        
        self.params['temp_1'] =  parameter('temp',idx=1,y_label='Temperature (C)',p_title="EPS temperature T1")
        self.params['temp_2'] =  parameter('temp',idx=2,y_label='Temperature (C)',p_title="EPS temperature T2")
        
        self.params['temp_3'] =  parameter('temp',idx=3,y_label='Temperature (C)',p_title="EPS temperature T3")
        
        self.params['temp_4'] =  parameter('temp',idx=4,y_label='Temperature (C)',p_title="Battery temperature") #battery temperature
        self.params['temp_5'] =  parameter('temp',idx=5,y_label='Temperature (C)',p_title="EPS temperature T5")
        
        # Solar power input
        self.params['Vin_0'] = parameter('vboost',idx=0,node=2,y_label="Voltage (mV)",p_title= "Input voltage 0") #node = 2 by default here
        self.params['Vin_1'] = parameter('vboost',idx=1,node=2,y_label="Voltage (mV)",p_title= "Input voltage 1")
        self.params['Vin_2'] = parameter('vboost',idx=2,node=2,y_label="Voltage (mV)",p_title= "Input voltage 2")
        self.params['Cin_0'] = parameter('curin',idx=0,node=2,y_label='Current (mA)',p_title='Input current 0') 
        self.params['Cin_1'] = parameter('curin',idx=1,node=2,y_label='Current (mA)',p_title='Input current 1') 
        self.params['Cin_2'] = parameter('curin',idx=2,node=2,y_label='Current (mA)',p_title='Input current 2')      
        
        # Power output
        self.params['V_obc'] = parameter('out_val',idx=0,node=2, y_label='Enable',p_title="Supply to OBC") 
        self.params['V_radio'] = parameter('out_val',idx=3,node=2, y_label='Enable',p_title="Supply to Radio") 
        self.params['V_payload'] = parameter('out_val',idx=5,node=2, y_label='Enable',p_title="Supply to Payload") 
        self.params['C_obc'] = parameter('curout',idx=0,node=2, y_label='Current (mA)',p_title="Supply current to OBC") 
        self.params['C_radio'] = parameter('curout',idx=3,node=2, y_label='Current (mA)',p_title="Supply current to Radio") 
        self.params['C_payload'] = parameter('curout',idx=5,node=2, y_label='Current (mA)',p_title="Supply current to Payload") 
        
        
        
        self.params['battmode'] = parameter('battmode',y_label="mode", p_title="Battery mode") 


        # Watchdog timers and bootcauses
        self.params['wdt_i2c'] = parameter('wdtI2cS',y_label="value",p_title="I2c watchdog timer") 
        self.params['wdt_GND'] = parameter('wdtGndS',y_label="value",p_title="Ground watchdog timer") 
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

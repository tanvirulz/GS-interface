import datetime
import pymongo
from pymongo import MongoClient

import Param
from Param import parameter



class SPEQS:
    
    def __init__(self, dbname = 'CQT', start_time=None, end_time=None):
        
        self.dbname = dbname
        self.st = start_time
        self.et = end_time
        
        self.client = None
        self.db = None

        self.Ts_conditions = {}
        self.common_conditions = {}
        
        self.params = {}

        self.params['en_payload'] = parameter('en_payload')               
        self.params['file_no'] = parameter('file_no')
        self.params['exp_profile'] = parameter('exp_profile')
        self.params['force_start'] = parameter('force_start')               
        self.params['exp_delay_s'] = parameter('exp_delay_s')  
        self.params['en_pheating'] = parameter('en_pheating')               
        self.params['pheat_tout'] = parameter('pheat_tout')               
        self.params['heater_setpt'] = parameter('heater_setpt')               
        self.params['fixed_LCPR'] = parameter('fixed_LCPR')               
        self.params['LD_current'] = parameter('LD_current')               
        self.params['exp_time'] = parameter('exp_time')               
        self.params['LCPR_ref'] = parameter('LCPR_ref')               
        self.params['LCPR_step'] = parameter('LCPR_step')               
        self.params['loop_counter'] = parameter('loop_counter')               
        self.params['btr'] = parameter('btr')                             
        self.params['APD1_offset'] = parameter('APD1_offset')                             
        self.params['APD2_offset'] = parameter('APD2_offset')                             
        self.params['LCPR1_buf_0'] =  parameter('LCPR1_Buf',idx=0)
        self.params['LCPR1_buf_1'] =  parameter('LCPR1_Buf',idx=1)
        self.params['LCPR1_buf_2'] =  parameter('LCPR1_Buf',idx=2)                            
        self.params['LCPR1_buf_3'] =  parameter('LCPR1_Buf',idx=3) 
        self.params['LCPR2_buf_0'] =  parameter('LCPR2_Buf',idx=0)
        self.params['LCPR2_buf_1'] =  parameter('LCPR2_Buf',idx=1)
        self.params['LCPR2_buf_2'] =  parameter('LCPR2_Buf',idx=2)                            
        self.params['LCPR2_buf_3'] =  parameter('LCPR2_Buf',idx=3)         
        
        
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

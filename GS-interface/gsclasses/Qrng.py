import datetime
import pymongo
from pymongo import MongoClient

import Param
from Param import parameter


class QRNG:
    
    def __init__(self, dbname = 'CQT', start_time=None, end_time=None):
        
        self.dbname = dbname
        self.st = start_time
        self.et = end_time
        
        self.client = None
        self.db = None

        self.Ts_conditions = {}
        self.common_conditions = {}
        
        self.params = {}

        self.params['active'] = parameter('active')               
        self.params['paramUpdIntval'] = parameter('paramUpdIntval')               
        self.params['curSending'] = parameter('curSending')               
        self.params['curQueueCnt'] = parameter('curQueueCnt')               
        self.params['curFilePos'] = parameter('curFilePos')               
        self.params['fileTimeStart'] = parameter('fileTimeStart')               
        self.params['fileReachEnd'] = parameter('fileReachEnd')               
        self.params['curFile'] = parameter('curFile')               
        self.params['curTime'] = parameter('curTime') 

        for index in range(32):
            self.params['prevData_'+ str(index)] = parameter('prevData',idx=index)
            self.params['curData_'+ str(index)] = parameter('curData',idx=index)

    #    self.params['LCPR1_buf_0'] =  parameter('LCPR1_Buf',idx=0 
        
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

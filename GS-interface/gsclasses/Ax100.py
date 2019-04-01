import datetime
import pymongo
from pymongo import MongoClient

import Param
from Param import parameter


class AX100:
    
    def __init__(self, dbname = 'CQT', start_time=None, end_time=None):
        
        self.dbname = dbname
        self.st = start_time
        self.et = end_time
        
        self.client = None
        self.db = None

        self.Ts_conditions = {}
        self.common_conditions = {}
        
        self.params = {}
        
        self.params['temp_brd'] = parameter('temp_brd')
        self.params['temp_pa'] = parameter('temp_pa')
        self.params['last_rssi'] = parameter('last_rssi')
        self.params['last_rferr'] = parameter('last_rferr')
        self.params['bgnd_rssi'] = parameter('bgnd_rssi')
        self.params['tx_duty'] = parameter('tx_duty')
        self.params['tot_tx_cnt'] = parameter('tot_tx_count')
        self.params['tot_rx_cnt'] = parameter('tot_rx_count')
        self.params['tot_tx_bytes'] = parameter('tot_tx_bytes')
        self.params['tot_rx_bytes'] = parameter('tot_rx_bytes')
        self.params['boot_count'] = parameter('boot_count')
        self.params['boot_cause'] = parameter('boot_cause')
        self.params['tx_bytes'] = parameter('tx_bytes')
        self.params['rx_bytes'] = parameter('rx_bytes')
        self.params['active_conf'] = parameter('active_conf')
        self.params['tx_count'] = parameter('tx_count')
        self.params['rx_count'] = parameter('rx_count')
              
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

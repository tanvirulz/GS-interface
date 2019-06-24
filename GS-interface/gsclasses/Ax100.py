import datetime
import pymongo
from pymongo import MongoClient

from gsclasses import Param
from gsclasses.Param import parameter

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
        
        self.params['temp_brd'] = parameter('temp_brd', y_label="Temperature (C)",p_title="Ax100 board temperature",n_factor=0.1)
        self.params['temp_pa'] = parameter('temp_pa', y_label="Temperature (C)",p_title="Ax100 temperature near PA",n_factor=0.1)
        self.params['last_rssi'] = parameter('last_rssi', y_label='rssi (dB)',p_title="Last_rssi")
        self.params['last_rferr'] = parameter('last_rferr')
        self.params['bgnd_rssi'] = parameter('bgnd_rssi')
        self.params['tx_duty'] = parameter('tx_duty',y_label='duty cycle %')
        self.params['tot_tx_cnt'] = parameter('tot_tx_count',y_label='count')
        self.params['tot_rx_cnt'] = parameter('tot_rx_count',y_label='count')
        self.params['tot_tx_bytes'] = parameter('tot_tx_bytes',y_label='count')
        self.params['tot_rx_bytes'] = parameter('tot_rx_bytes',y_label='count')
        
        self.params['boot_count'] = parameter('boot_count',y_label='count')
        self.params['boot_cause'] = parameter('boot_cause',y_label='count')
        self.params['tx_bytes'] = parameter('tx_bytes',y_label='count')
        self.params['rx_bytes'] = parameter('rx_bytes',y_label='count')
        self.params['active_conf'] = parameter('active_conf',y_label='conf. id')
        self.params['tx_count'] = parameter('tx_count',y_label='count')
        self.params['rx_count'] = parameter('rx_count',y_label='count')
              
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

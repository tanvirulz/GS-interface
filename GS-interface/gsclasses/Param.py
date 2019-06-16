import pymongo
import time

#needed for test only
from random import shuffle

class parameter:
    def __init__(self,pname,idx=None,node=None,y_label="", p_title=None,n_factor = 1):
        self.name = pname
        self.Ts = None #ephoch time 
        self.sTs =None #time in string format
        self.Vals = None
        self.idx  = idx
        self.node = node
        self.y_label = y_label
        self.n_factor = n_factor
        if p_title is None :
            self.p_title = pname + ' vs. time'
        else:
            self.p_title = p_title 
    def getdata(self,db,Ts_conditions, idx=None, node=None):
        conditions = []
        if self.name is None:
            print ("parameter missing in getdata")
            return
        
        conditions.append({'Param.Name':str(self.name)})
        if self.idx is not None:
            conditions.append({'Param.Index': int(self.idx)})
        if self.node is not None:
            conditions.append( {'Param.Node': int(self.node)})
        
        conditions.append({'Ts':Ts_conditions})
        results = db.ParamData.find( {'$and':conditions} ).sort('Ts',pymongo.DESCENDING)
        
        self.Ts = []
        self.Vals = []
        self.sTs = [] 
        for x in results:   
            #[TODO] compare with the last value, if the jump is too big ignor, otherwise include. 
            #if x['Val'] == 0:
            #    continue 
            self.Ts.append(x['Ts'])
            self.sTs.append( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x['Ts'])) ) 
            self.Vals.append(x['Val']*self.n_factor)

    
    def status (self):
        print (self.name, "idx=",self.idx,"node=",self.node, "len(Ts)=",len(self.Ts),"len(Vals)=", len(self.Vals))

    '''
    helper function for testing
    '''
    def get_random(self,db,Ts_conditions, idx=None, node=None):
        self.Ts = list(range(10))
        self.Vals = list(range(10))
        shuffle(self.Vals )
        self.sTs = list(range(10))
        self.y_label = self.name + ' (unit)'
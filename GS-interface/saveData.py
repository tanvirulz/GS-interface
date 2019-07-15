

from gsclasses import Eps 

#st=1560716400 #start_time 17th June
st= 1562169600 #july 4 00:00 
#et=1561104130 #end_time 
#et=1561950429 #end_time  28th June
#et=1561976513 #end_time  1st July
#et=1562060929 # 2nd July

#et=1562123058 # 3rd July
#et=1562209657 #3th july
et = 1562577717 # July 8
#et = None 
#st = None
#et = None
DB_NAME = "SWGS13"
#DB_NAME = "SWGS"

eps = Eps.EPS(dbname=DB_NAME,start_time=st, end_time=et) 


#eps.test_load()
eps.reload()

eps.params['Cin_0'].to_csv("testcin0.csv")
eps.params['vbatt'].to_csv()


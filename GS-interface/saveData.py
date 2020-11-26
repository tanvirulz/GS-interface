

from gsclasses import Eps 
from gsclasses import Obc 
from gsclasses import Ax100
from gsclasses import Qrng


#st=1560716400 #start_time 17th June
#st= 1562169600 #july 4 00:00 
#st = 1559351975 #june 1

#st = 1561564800
#et=1561104130 #end_time
#et=1561950429 #end_time  28th June
#et=1561976513 #end_time  1st July
#et=1562060929 # 2nd July

#et = 1561651200
#et=1562123058 # 3rd July
#et=1562209657 #3th july
#et = 1562577717 # July 8
#et = None 
#st = None
#et = None
#et = 1568611945 #Sept 16
#st = 1568337665 #sept 13 2019
#et = 1568342532

st = 1527799087 #june 6 2018
#et = 1606366153 #26 Nov 2020 
et = 1606366153 #May 5 2020

DB_NAME = "SWGS50"
#DB_NAME = "SWGS"

eps = Eps.EPS(dbname=DB_NAME,start_time=st, end_time=et) 
obc = Obc.OBC(dbname=DB_NAME,start_time=st, end_time=et) 
ax100 = Ax100.AX100(dbname=DB_NAME,start_time=st, end_time=et)
qrng = Qrng.QRNG(dbname=DB_NAME,start_time=st, end_time=et)
qrng.reload()
#eps.test_load()
#eps.reload()

#eps.params['temp_0'].to_csv()
#eps.params['vbatt'].to_csv()
#obc.reload()
#ax100.reload()

#obc.params['temp_a'].to_csv()
#obc.params['temp_b'].to_csv()


#ax100.params['temp_brd'].to_csv()

#qrng.params['curData_1'].to_csv("paramdata1.csv")

for i in range (32):
    qrng.params["curData_"+str(i)].to_csv("SWZcurdata_"+str(i))



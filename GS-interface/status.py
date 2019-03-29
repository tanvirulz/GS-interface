
import Eps


eps = Eps.EPS()
eps.connect()
eps.reload()


#print (eps.params['vbatt'].sTs[0] )

for pname,param in eps.params.items():
    print (pname, "\t:", end='')
    param.status()


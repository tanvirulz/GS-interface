import numpy as np

def piecewise_integrate(y,x,integration_start,period,count):
    ry = []
    rx = []
    for i in range(count-1):
        #print("test")
        #print(integration_start+i*period)
        a = integration_start+i*period
        #print(a)
        b = integration_start+(i+1)*period
        #print(b)
        ai =  np.searchsorted(x, a, side='left', sorter=None)
        #print (ai)
        #print (x)
        bi =  np.searchsorted(x, b, side='left', sorter=None)
        np.trapz(y[ai:bi], x[ai:bi])
        ry.append(np.trapz(y[ai:bi], x[ai:bi])) 
        rx.append(int(a+b)/2)
    return ry, rx 

def normalize(x,y,z):
    nx = []
    ny = []
    nz = []
    for i in range(len(x)):
        tot = x[i]+y[i]+z[i]-94560 #94560 is the correction term of the z values. The Z solar panel has some valuse during the eclipse. 
                                #This is an attempt to remove that by integrating the curve under eclipse 
                                # and subtracting the result form whole orbit integration.
        nx.append(x[i]*100.0/tot)
        ny.append(y[i]*100.0/tot)
        nz.append( (z[i]-94560)*100.0/tot)
    return nx,ny,nz 

    
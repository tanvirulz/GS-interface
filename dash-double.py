import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import time
import datetime
from pymongo import MongoClient
import pymongo


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#x1 = [ 1,2,3,4]
#y1 = [0.04,0.06,0.03,0.08]

def getdata(pname,idx=None,node=None,st=None,et=None,scaling_factor=1):
    client = MongoClient('localhost',27017)
    db = client.CQT
    conditions =[]
    if pname is None:
        print ("parameter missing in getdata")
        return
    
    conditions.append({'Param.Name':str(pname)})
    
    if idx is not None:
        conditions.append({'Param.Index': int(idx)})
    if node is not None:
        conditions.append( {'Param.Node': int(node)})

    Ts_conditions = {}

    if st is not None:
        Ts_conditions['$gte'] = int(st)
    else:
        Ts_conditions['$gte'] = int(1452160013) #GMT: Thursday, January 7, 2016 9:46:53 AM
    if et is not None:
        Ts_conditions['$lt'] = int(et)

    conditions.append({'Ts':Ts_conditions})

    results = db.ParamData.find( {'$and':conditions} ).sort( { "Ts": pymongo.DESCENDING } )
    
    Ts = []
    Vals = []
    for x in results:    
        Ts.append(x['Ts'])
        Vals.append(x['Val']/scaling_factor)

    client.close()
    
    return Ts, Vals, pname, idx, node



axis_dict = {
    "vbatt": "Voltage (V)",
    "temp": "Temp (C)",        
    "boot_count": "Counts"
}


Ts, Val, pname,idx, node = getdata(pname='temp',idx=0)  #,st=1546844400,et=1547535600)      
Ts2,Val2,pname2,idx2, node2 = getdata(pname='boot_count',node=5)   #,st=1546844400,et=1547535600)     

Tsdt = [ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x)) for x in Ts]

Tsdt2 = [ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x)) for x in Ts2]
#Val2_scaled = [ x/1000 for x in Val2]

trace1 = go.Scatter(
    x=Tsdt,
    y=Val,
    name=pname+"_"+ str(idx)
)
trace2 = go.Scatter(
    x=Tsdt2,
    y=Val2,
    name=pname2,
    yaxis='y2'
)
data = [trace1, trace2]

layout = go.Layout(
    title= "Plot: "+pname+" and "+pname2,
    yaxis=dict(
        title=axis_dict[pname]
    ),
    yaxis2=dict(
        title=axis_dict[pname2],
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)





app.layout = html.Div(children=[
    html.H1(children='GS-Dash'),

    html.Div(children='''
        SpooQySat: Ground station data interface
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': data,
            'layout': layout
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True) 

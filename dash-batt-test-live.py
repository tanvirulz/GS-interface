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
    db = client.CQT2
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

    results = db.ParamData.find( {'$and':conditions} ).sort('Ts',pymongo.DESCENDING)
    
    Ts = []
    Vals = []
    for x in results:   
        if x['Val'] == 0:
            continue 
        Ts.append(x['Ts'])
        Vals.append(x['Val']/scaling_factor)

    client.close()
    if idx is None:
        idx = ""
    else:
        idx = "_" + str(idx)
    return Ts, Vals, pname, idx, node



axis_dict = {
    "vbatt": "Voltage (V)",
    "temp": "Temp (C)",        
    "boot_count": "Counts"
}


#Ts, Val, pname,idx, node = getdata(pname='temp',idx=0)  #,st=1546844400,et=1547535600)      
#Ts2,Val2,pname2,idx2, node2 = getdata(pname='boot_count',node=5)   #,st=1546844400,et=1547535600)  

#Ts, Val, pname,idx, node = getdata(pname='temp',idx=4,st=1546844400,et=1547535600)      
#Ts2,Val2,pname2,idx2, node2 = getdata(pname='vbatt', st=1546844400,et=1547535600,scaling_factor=1000)        

#Ts, Val, pname,idx, node = getdata(pname='vbatt', st=1547125837,et=1548868330,scaling_factor=1000)        
#Ts2,Val2,pname2,idx2, node2 = getdata(pname='temp',idx=4,st=1547125837,et=1548868330)      



def reload_on_refresh_layout():

    phase = " Charging"
    name_before = "_before_vibration"
    name_after = "_after_vibration"
    #Battery Charging before
    Ts, Val, pname,idx, node = getdata(pname='vbatt', st=1547323972,et=1547436652,scaling_factor=1000)        
    Ts2,Val2,pname2,idx2, node2 = getdata(pname='vbatt',st=1547899228,et=1548011548,scaling_factor=1000)      
    pname_legend = pname + name_before
    pname_legend2 = pname2 + name_after

    #Ts2,Val2,pname2,idx2, node2 = getdata(pname='boot_count',node=5, st=1546844400,et=1547535600,scaling_factor=1)        
    Ts_delta = [(x-1547323972) for x in Ts]
    Tsdt = Ts_delta#[datetime.timedelta(x) for x in Ts_delta]
    #Tsdt = [ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x)) for x in Ts]

    Ts2_delta = [(x-1547899228-400) for x in Ts2]
    Tsdt2 = Ts2_delta#[datetime.timedelta(x) for x in Ts2_delta]
    #Tsdt2 = [ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x)) for x in Ts2]
    #Val2_scaled = [ x/1000 for x in Val2]
    #import datetime
    #>>> str(datetime.timedelta(seconds=666))
    #'0:11:06'

    trace1 = go.Scatter(
        x=Tsdt,
        y=Val,
        name=pname_legend.capitalize()+str(idx),
    )
    trace2 = go.Scatter(
        x=Tsdt2,
        y=Val2,
        name=pname_legend2.capitalize()+str(idx2),
        #yaxis='y2'
    )
    data = [trace1, trace2]

    layout = go.Layout(
        title= "Plot: "+pname.capitalize()+phase,
        xaxis=dict(
            title='Time (s)'
        ),    
        yaxis=dict(
            title=axis_dict[pname],
        
        
        ),
        yaxis2=dict(
            title=axis_dict[pname2],
            titlefont=dict(
                color='rgb(148, 103, 189)'
            ),
            tickfont=dict(
                color='rgb(148, 103, 189)'
            ),
            showgrid=False,
            #overlaying='y',
            #side='right'
        )
    )




   
    app_layout = html.Div(children=[
        html.H1(children='GS-Dash'),
        html.H2('Data loaded at: ' + str(datetime.datetime.now())),
        html.Div(children='SpooQySat: Ground station data interface'
            ),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': data,
                'layout': layout
            }
        )
    ])
    return app_layout 

app.layout = reload_on_refresh_layout
'''
app.layout = html.Div(children=[
    html.H1(children='GS-Dash'),
    #html.H1('The time is: ' + str(datetime.datetime.now())),
    html.Div(children='
        SpooQySat: Ground station data interface
    '),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': data,
            'layout': layout
        }
    )
])
'''
if __name__ == '__main__':
    app.run_server(debug=True) 
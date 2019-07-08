#from gsclasses import *

#import gsclasses.Param

import dash
import dash_core_components as dcc
import dash_html_components as html


import plotly.graph_objs as go

import time
import datetime

def gen_context_fig(container,pname):
    if pname == 'Cin_comb':
        return html.Div(className="figure",children=[
            dcc.Graph(
                id='context-plot',
                figure={
                    'data': [{
                        'x': container.params["Cin_0"].sTs,
                        'y': container.params["Cin_0"].Vals,
                        #'type': 'bar',
                        'type': 'scatter',
                        'name': 'X',
                    },
                    {
                        'x': container.params["Cin_1"].sTs,
                        'y': container.params["Cin_1"].Vals,
                        #'type': 'bar',
                        'type': 'scatter',
                        'name': 'Y',
                    },
                    {
                        'x': container.params["Cin_2"].sTs,
                        'y': container.params["Cin_2"].Vals,
                        #'type': 'bar',
                        'type': 'scatter',
                        'name': 'Z',
                    }
                    
                    ],
                    'layout': go.Layout(
                        xaxis={'title': 'Time'},
                        yaxis={ 'title': 'current (mA)'}, #'title': container.params["Cin_0"].y_label},
                        #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                        #legend={'x': 0, 'y': 1},
                        title = "input current from solar panels", #container.params["Cin_0"].p_title,
                        hovermode='closest'
                    )
                    #'layout': {
                    #'title': container.params[pname].p_title,
                    #'xaxis': "time"
                    #}

                }
            )

        ])

    return html.Div(className="figure",children=[
        dcc.Graph(
            id='context-plot',
            figure={
                'data': [{
                    'x': container.params[pname].sTs,
                    'y': container.params[pname].Vals,
                    #'type': 'bar',
                    'type': 'scatter'
                }],
                'layout': go.Layout(
                    xaxis={'title': 'Time'},
                    yaxis={'title': container.params[pname].y_label},
                    #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    #legend={'x': 0, 'y': 1},
                    title = container.params[pname].p_title,
                    hovermode='closest'
                )
                #'layout': {
                #'title': container.params[pname].p_title,
                #'xaxis': "time"
                #}

            }
        )
    ])

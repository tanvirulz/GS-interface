#import Eps
#import Param

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

import time
import datetime


def obc_context_fig(obc,tab):
    if tab == 'obc-temp_a':
        return html.Div(className="figure",children=[
            dcc.Graph(
                id='context-plot',
                figure={
                    'data': [{
                        #x=eps.params['vbatt'].sTs, 
                        #y=eps.params['vbatt'].Vals,
                        'x': obc.params['temp_a'].sTs,
                        'y': obc.params['temp_a'].Vals,
                        'type': 'scatter'
                    }]
                }
            )
        ])
    '''
    elif tab == "eps-c-obc":
        return html.Div(className="figure",children=[
            dcc.Graph(
                id='context-plot',
                figure={
                    'data': [{
                        #x=eps.params['vbatt'].sTs, 
                        #y=eps.params['vbatt'].Vals,
                        'x': eps.params['C_obc'].sTs,
                        'y': eps.params['C_obc'].Vals,
                        'type': 'scatter'
                    }]
                }
            )
        ])
    '''

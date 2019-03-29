import Eps
import Param

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

import time
import datetime


def eps_context_fig(eps,tab):
    if tab == 'eps-vbatt':
        return html.Div(className="figure",children=[
            dcc.Graph(
                id='context-plot',
                figure={
                    'data': [{
                        #x=eps.params['vbatt'].sTs, 
                        #y=eps.params['vbatt'].Vals,
                        'x': eps.params['vbatt'].sTs,
                        'y': eps.params['vbatt'].Vals,
                        'type': 'scatter'
                    }]
                }
            )
        ])
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
    elif tab == "eps-c-radio":
        return html.Div(className="figure",children=[
            dcc.Graph(
                id='context-plot',
                figure={
                    'data': [{
                        #x=eps.params['vbatt'].sTs, 
                        #y=eps.params['vbatt'].Vals,
                        'x': eps.params['C_radio'].sTs,
                        'y': eps.params['C_radio'].Vals,
                        'type': 'scatter'
                    }]
                }
            )
        ])
    

def eps_context_info(eps,tab,main_tab=""):
    return html.Table([
        html.Tr([
            html.Td([
                "Battery Mode"
            ]),
            html.Td([
                str(eps.params["battmode"].Vals[-1])
            ])
        ], style={'border': '1px solid black'}),
        html.Tr([
            html.Td([
                "wdt_i2c"
            ]),
            html.Td([
                #str(eps.params["wdt_i2c"].Vals[-1])
                main_tab
            ])
        ],style={'border': '1 black'}),

    ])
 
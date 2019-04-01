import dash
import dash_core_components as dcc
import dash_html_components as html


import plotly.graph_objs as go

import time
import datetime


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
 

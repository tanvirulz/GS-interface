import Param

import dash
import dash_core_components as dcc
import dash_html_components as html


import plotly.graph_objs as go

import time
import datetime

def gen_context_fig(container,pname):
    return html.Div(className="figure",children=[
        dcc.Graph(
            id='context-plot',
            figure={
                'data': [{
                    'x': container.params[pname].sTs,
                    'y': container.params[pname].Vals,
                    'type': 'scatter'
                }]
            }
        )
    ])
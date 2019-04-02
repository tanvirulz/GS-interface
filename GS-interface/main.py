'''
Experiment with css grid layout with dash using python3 
'''
'''
    TODO 
    - Add all the main tabs
    - Identify the sub-tabs to be shown
    - Implement all the sub-tabs
    - Add documentation
    - Refresh button
    - Time selection
    - Link-up to the main server
'''

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

import time
import datetime


#custom display modules


from gsclasses import Eps
from gsclasses import Obc


#import Eps
#from DisplayEPS import *

from contextTabs import *
from contextInfoGen import eps_context_info
from contextFigGen import gen_context_fig



app = dash.Dash(__name__)

eps = Eps.EPS()
#eps.reload()
eps.test_load()

obc = Obc.OBC()
obc.test_load()

app.layout = html.Div([
    html.H1("SpooQy-1 Ground Station"),
    html.P("Hit refresh to reload"),
    
    html.Div(
        className="grid-container",
        children=[
            html.Div(
                className="mainheader",
                children=[
                    dcc.Tabs(id="main-tabs", value='main-eps', children=[
        
                        dcc.Tab(label='EPS', value='main-eps'),
                        dcc.Tab(label='OBC', value='main-obc'),
                        dcc.Tab(label='AX100', value='main-ax100'),
    
                    ]),
                ]
                
            ),
            html.Div(
                className="info",
                children="info"
            ),
            html.Div(
                className="subheader",
                id="context-sub-tabs",
                children=[
                    dcc.Tabs(id="context-tabs",),
                ]
            ),
            html.Div(
                className="contextinfo",
                id="tab-context-info"
            ),
            html.Div(
                className="figure",
                id="tab-context-plot"

            )

        ]
    ),


])

@app.callback(Output('context-tabs', 'value'),
              [Input("main-tabs", 'value')])
def select_default_context_tab(main_tab):
    if main_tab == "main-eps": return 'eps-vbatt'
    elif main_tab == "main-obc": return 'obc-temp_a'
    elif main_tab == "main-ax100": return 'ax-val1'

@app.callback(Output('context-tabs', 'children'),
              [Input("main-tabs", 'value')])
def render_context_tabs(main_tab):
    return genContextTabs(main_tab)



@app.callback(Output('tab-context-info', 'children'),
              [Input("context-tabs", 'value'),Input("main-tabs", 'value')])
def render_context_info(tab,main_tab):
    #return eps_context_info(eps,tab,main_tabs)
    return main_tab
    

@app.callback(Output('tab-context-plot', 'children'),
              [Input("context-tabs", 'value'),Input("main-tabs", 'value')])
def render_context_plot(tab,main_tab):
    if main_tab == 'main-eps': return gen_context_fig(eps, tab[4:] )
    elif main_tab == 'main-obc':return gen_context_fig(obc,tab[4:])
    
            



if __name__ == '__main__':
    app.run_server(debug=True)

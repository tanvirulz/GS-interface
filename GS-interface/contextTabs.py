#from gsclasses import Eps
#from gsclasses import Param
#import Eps
#import Param

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

import time
import datetime

def genContextTabs(main_tab):
    if main_tab == "main-eps": 
        return [
            dcc.Tab(label='vbatt', value='eps-vbatt'),
            dcc.Tab(label='c-obc', value='eps-C_obc'),
            dcc.Tab(label='c-radio', value='eps-C_radio'), #temp_0
            dcc.Tab(label='temp_0', value='eps-temp_0'),
            dcc.Tab(label='temp_1', value='eps-temp_1'),
            dcc.Tab(label='temp_2', value='eps-temp_2'),
            dcc.Tab(label='temp_3', value='eps-temp_3'),
            dcc.Tab(label='temp_4', value='eps-temp_4'),
            dcc.Tab(label='temp_5', value='eps-temp_5'), #C_payload
            dcc.Tab(label='C_payload', value='eps-C_payload'),
        ]
    elif main_tab == "main-obc":
        return [
            dcc.Tab(label='temp_a', value='obc-temp_a'),
            dcc.Tab(label='oval2', value='obc-oval2'),
        ]
    elif main_tab == "main-ax100":
        return [
            dcc.Tab(label='ax1', value='ax-val1'),
            dcc.Tab(label='ax2', value='ax-val2'),
        ]

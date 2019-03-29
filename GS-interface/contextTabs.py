import Eps
import Param

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
            dcc.Tab(label='c-obc', value='eps-c-obc'),
            dcc.Tab(label='c-radio', value='eps-c-radio'),
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
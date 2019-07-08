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
            #dcc.Tab(label='temp_1', value='eps-temp_1'),
            #dcc.Tab(label='temp_2', value='eps-temp_2'),
            #dcc.Tab(label='temp_3', value='eps-temp_3'),
            #dcc.Tab(label='temp_4', value='eps-temp_4'),
            #dcc.Tab(label='temp_5', value='eps-temp_5'), 
            
            #solar panel inputs
            dcc.Tab(label='Vin_0', value='eps-Vin_0'),
            dcc.Tab(label='Vin_1', value='eps-Vin_1'),
            dcc.Tab(label='Vin_2', value='eps-Vin_2'),
            dcc.Tab(label='Cin_0', value='eps-Cin_0'),
            dcc.Tab(label='Cin_1', value='eps-Cin_1'),
            dcc.Tab(label='Cin_2', value='eps-Cin_2'),
            dcc.Tab(label='Cin_combined', value='eps-Cin_comb'),
            
            dcc.Tab(label='boot_cnt', value='eps-boot_cnt'),

            #power output
            dcc.Tab(label='C_payload', value='eps-C_payload'),
            dcc.Tab(label='V_payload', value='eps-V_payload'),
            dcc.Tab(label='C_obc', value='eps-C_obc'),
            dcc.Tab(label='V_obc', value='eps-V_obc'),
            dcc.Tab(label='C_radio', value='eps-C_radio'),
            dcc.Tab(label='V_radio', value='eps-V_radio'),

        ]
    elif main_tab == "main-obc":
        return [
            dcc.Tab(label='temp_a', value='obc-temp_a'),
            dcc.Tab(label='temp_b', value='obc-temp_b'),
            
            dcc.Tab(label='pwrGSSB1', value='obc-pwrGSSB1'),
            dcc.Tab(label='pwrGSSB2', value='obc-pwrGSSB2'),
            dcc.Tab(label='pwrflash', value='obc-pwrflash'),
            dcc.Tab(label='pwrPWM', value='obc-pwrPWM'),

            dcc.Tab(label='curGSSB1', value='obc-curGSSB1'),
            dcc.Tab(label='curGSSB2', value='obc-curGSSB2'),
            dcc.Tab(label='curflash', value='obc-curflash'),
            dcc.Tab(label='curPWM', value='obc-curPWM'),
        ]
    elif main_tab == "main-ax100":
        return [
            dcc.Tab(label='temp_brd', value='ax1-temp_brd'),
            dcc.Tab(label='temp_pa', value='ax1-temp_pa'),
            
            
            dcc.Tab(label='tx_duty', value='ax1-tx_duty'),
            dcc.Tab(label='tx_count', value='ax1-tx_count'),
            dcc.Tab(label='rx_count', value='ax1-rx_count'),
            
            
            dcc.Tab(label='tot_tx_cnt', value='ax1-tot_tx_cnt'),
            dcc.Tab(label='tot_rx_cnt', value='ax1-tot_rx_cnt'),
            dcc.Tab(label='tot_tx_bytes', value='ax1-tot_tx_bytes'),

            dcc.Tab(label='boot_count', value='ax1-boot_count'),

        ]
    elif main_tab == "main-adcs":
        return [
            dcc.Tab(label='gyro_0', value='adc-gyro_0'),
            
            dcc.Tab(label='gyro_1', value='adc-gyro_1'),
            dcc.Tab(label='gyro_2', value='adc-gyro_2'),
            dcc.Tab(label='gyro_tr_0', value='adc-gyro_trend_0'),
            dcc.Tab(label='gyro_tr_1', value='adc-gyro_trend_1'),
            dcc.Tab(label='gyro_tr_2', value='adc-gyro_trend_2'),
            dcc.Tab(label='gyro_temp', value='adc-gyro_temp'),
            dcc.Tab(label='gyro_valid', value='adc-gyro_valid'),

            dcc.Tab(label='mag_0', value='adc-mag_0'),
            dcc.Tab(label='mag_1', value='adc-mag_1'),
            dcc.Tab(label='mag_2', value='adc-mag_2'),
            dcc.Tab(label='mag_valid', value='adc-mag_valid'),



            dcc.Tab(label='suns_temp_0', value='adc-suns_temp_0'),
            
            
            #dcc.Tab(label='suns_temp_1', value='adc-suns_temp_1'),
            #dcc.Tab(label='suns_temp_2', value='adc-suns_temp_2'),
            #dcc.Tab(label='suns_temp_3', value='adc-suns_temp_3'),
            #dcc.Tab(label='suns_temp_4', value='adc-suns_temp_4'),
            #dcc.Tab(label='suns_temp_5', value='adc-suns_temp_5'),
            
            #dcc.Tab(label='mag_valid', value='adc-mag_valid'),



            #dcc.Tab(label='torquer_duty_0', value='adc-torquer_duty_0'),
            #dcc.Tab(label='torquer_duty_1', value='adc-torquer_duty_1'),
            #dcc.Tab(label='torquer_duty_2', value='adc-torquer_duty_2'),
            #dcc.Tab(label='bdot_detumb', value='adc-bdot_detumb'),
            
        ]

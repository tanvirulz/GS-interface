import dash
import dash_core_components as dcc
import dash_html_components as html


import plotly.graph_objs as go

import time
import datetime

from dataTableHelper import table_elem


def eps_context_info(eps,obc,ax100,adcs,tab,main_tab=""):
    if main_tab == 'main-eps': 
        return html.Div( children=[ 
            html.H3("EPS info"),
            html.Table([
                table_elem ("wdt_i2c:", eps.params["wdt_i2c"].Vals[-1]),
                table_elem ("cntWdtI2c:", eps.params["cntWdtI2c"].Vals[-1]),
                table_elem ("cntWdtCsp_0:",  eps.params["cntWdtCsp_0"].Vals[-1]),
                table_elem ("bootCause:",  eps.params["bootCause"].Vals[-1]),
            ]),        
            
        ])   
    elif main_tab == 'main-obc': 
        return html.Div( children=[ 
            html.H3("OBC info"),
            html.Table([
                table_elem ("swload_count:", obc.params["swload_count"].Vals[-1]),
                table_elem ("fs_mounted:", obc.params["fs_mounted"].Vals[-1]),
                table_elem ("boot_count:",  obc.params["boot_count"].Vals[-1]),
                table_elem ("clock:",  obc.params["clock"].Vals[-1]),
            ]),        
        ]) 
    elif main_tab == 'main-ax100': 
        return html.Div( children=[ 
            html.H3("AX100 info"),
            html.Table([
                table_elem ("boot_count:", ax100.params["boot_count"].Vals[-1]),
                table_elem ("boot_cause:", ax100.params["boot_cause"].Vals[-1]),
                table_elem ("active_conf:",  ax100.params["active_conf"].Vals[-1]),
                
            ]),        
        
        ]) 
    elif main_tab == 'main-adcs': 
        return html.Div( children=[ 
            html.H3("ADCS info"),
            html.Table([
                table_elem ("status_mag:", adcs.params["status_mag"].Vals[-1]),
                table_elem ("status_css:", adcs.params["status_css"].Vals[-1]),
                table_elem ("status_gyro:",  adcs.params["status_gyro"].Vals[-1]),
                table_elem ("status_bdot:",  adcs.params["status_bdot"].Vals[-1]),
                table_elem ("status_run:",  adcs.params["status_run"].Vals[-1]),
                table_elem ("looptime:",  adcs.params["looptime"].Vals[-1]),
                table_elem ("maxlooptime:",  adcs.params["maxlooptime"].Vals[-1]),
            ]),  
        ]) 

    else: return main_tab
    '''    
    return gen_context_fig(eps, tab[4:])
    elif main_tab == 'main-obc':return gen_context_fig(obc,tab[4:])
    elif main_tab == 'main-ax100': return gen_context_fig(ax100,tab[4:])
    elif main_tab == 'main-adcs': return gen_context_fig(adcs,tab[4:])
    '''
    '''
    return html.Div( children=[ 
        html.H3("power_input"),
        html.Table([
            table_elem ("CH1(11.7V):", eps.params["Cin_0"].Vals[-1], "mA"),
            table_elem ("CH2(11.7V):", eps.params["Cin_1"].Vals[-1], "mA"),
            table_elem ("CH3(3.3V):",  eps.params["Cin_2"].Vals[-1], "mA"),
            
        ]),
        html.H3("power_output"),
        html.Table([
            table_elem ("OBC(3.3V):", eps.params["C_obc"].Vals[-1], "mA"),
            table_elem ("AX100(3.3V):", eps.params["C_radio"].Vals[-1], "mA"),
            table_elem ("V_payload(5V):", eps.params["C_payload"].Vals[-1], "mA"),
           
            table_elem ("Battery mode:", eps.params["battmode"].Vals[-1], "mA"),
        ]),
        html.Hr(),
        html.Table([
            table_elem ("Battery mode:", eps.params["battmode"].Vals[-1]),
            table_elem ("Battery voltage:", eps.params["vbatt"].Vals[-1]/1000, "V"),
            table_elem ("EPS ground watchdog:", eps.params["wdt_GND"].Vals[-1]),
            table_elem ("EPS Boot count:", eps.params["boot_cnt"].Vals[-1]),
        ]),
        html.Hr(),
        html.Table([
            table_elem ("OBC temp A:", obc.params["temp_a"].Vals[-1]),
            table_elem ("OBC Boot count:", obc.params["boot_count"].Vals[-1]/1000, "V"),
        ])
    ])

         
    '''
    '''
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
    '''
 

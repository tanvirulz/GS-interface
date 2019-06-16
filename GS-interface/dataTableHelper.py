import dash_html_components as html

def table_elem (field,val,unit=''):
    return html.Tr([
        html.Td([
            str(field)
        ]),
        html.Td([
            str(val) +' '+ str(unit)
        ])
    ])


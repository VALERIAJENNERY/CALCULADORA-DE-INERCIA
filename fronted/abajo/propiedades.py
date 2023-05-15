from dash import html # importar dash 
import dash_bootstrap_components as dbc #importar los componentes del Bootstrap


# Se crea una lista de propiedades 

row1 = html.Tr([html.Td("Inercía (Iy)"), html.Td("10")])
row2 = html.Tr([html.Td("Inercía (Ix)"), html.Td("20")])
row3 = html.Tr([html.Td("Área (A)"), html.Td("30")])
row4 = html.Tr([html.Td("Centroide x (Cx)"), html.Td("40")])
row5 = html.Tr([html.Td("Centroide y (Cy)"), html.Td("50")])
row6 = html.Tr([html.Td("Constante Torsional (J)"), html.Td("60")])

table_body = [html.Tbody([row1, row2, row3, row4,row5,row6])]

table = dbc.Table( table_body, bordered=True,
    style={'background-color': 'white', 
                               "font-family": "Arial Narrow", 
                               "color": "purple", 
                               "font-weight": "bold", 
                               "text-align": "center",
                               'border': '0.5px solid purple'}
)

propiedades = html.Div(
    [  # Se crea una fila.
        dbc.Row(
            [
                dbc.Col('PROPIEDADES GEOMÉTRICAS', md=12, style ={'background-color': 'purple', 
                               "font-family": "Arial Narrow", 
                               "color": "white", 
                               "font-weight": "bold", 
                               "text-align": "center",
                               'border': '0.5px solid purple',
                               'margin-bottom': '10px'}) # Se crea una columna con el titulo.
            ],
        ), 
        dbc.Row(
            [
                dbc.Col(html.Div(
                    dbc.Row(
                        dbc.Col(table, width={'size': 8, 'offset': 0}),justify='center')
    ),
    style={'background-color': '#C88DD'}
)
            ],
        ), 
])


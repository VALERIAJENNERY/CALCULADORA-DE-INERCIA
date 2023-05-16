from dash import html # importar dash 
import dash_bootstrap_components as dbc #importar los componentes del Bootstrap
from fronted.datos.datos_rec import *


# Se crea una lista de propiedades para rectangulo

row1_rec = html.Tr([html.Td("Inercía (Iy)"), html.Td(iy_rectangulo)])
row2_rec = html.Tr([html.Td("Inercía (Ix)"), html.Td(ix_rectangulo)])
row3_rec = html.Tr([html.Td("Área (A)"), html.Td(area_rectangulo)])
row4_rec = html.Tr([html.Td("Centroide x (Cx)"), html.Td(cx_rectangulo)])
row5_rec = html.Tr([html.Td("Centroide y (Cy)"), html.Td(cy_rectangulo)])
row6_rec = html.Tr([html.Td("Constante Torsional (J)"), html.Td(j_rectangulo)])

table_body_rec = [html.Tbody([row1_rec, row2_rec, row3_rec, row4_rec,row5_rec,row6_rec])]

table_rec = dbc.Table( table_body_rec, bordered=True,
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
                        dbc.Col(table_rec, width={'size': 10, 'offset': 0}),justify='center',align='center')
    ),
    style={'background-color': '#C88DD'}
)
            ],
        ), 
])


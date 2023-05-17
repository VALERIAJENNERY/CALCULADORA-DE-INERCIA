from dash import html # importar dash 
import dash_bootstrap_components as dbc #importar los componentes del Bootstrap

from fronted.abajo.tablas import *

# Se crea una variable que contenga: 

abajo_Rec = dbc.Container(
    [
        dbc.Row( # Una fila 
            [ 
                dbc.Col(html.Div(
                            [  # Se crea una fila.
                                dbc.Row(
                                    [
                                        dbc.Col('GRAFICA', md=12, style ={'background-color': 'purple', 
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
                                        dbc.Col(id="salida_grafica_rec", style={'text-align': 'center'}) # Se crea una columna con el titulo.
                                    ],
                                ), 
                        ])), # Una columna con el nombre grafica 
                dbc.Col(html.Div(
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
                        ])),# Una columna con las propiedades geométricas
                
    ], 
        )
        
    ]
)
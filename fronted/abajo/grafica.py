from dash import html # importar dash 
import dash_bootstrap_components as dbc #importar los componentes del Bootstrap

contenido = html.Div(
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
])

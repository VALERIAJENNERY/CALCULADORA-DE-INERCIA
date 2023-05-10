from dash import html # Se importa dash 
import dash_bootstrap_components as dbc # Se importa los componentes deBootstrap 

# Se crea una variable que contenga: 
arriba = dbc.Container(

    [
        html.Hr(), # se le pone una división 
        html.H2("Seleccione una figura geométrica:",style={"font-family": "Arial Narrow", "color": "Black", "font-weight": "bold", "text-align": "center"}), # Se le pone un titulo. 
        html.Hr(), # se le pone una división 
    ]
)

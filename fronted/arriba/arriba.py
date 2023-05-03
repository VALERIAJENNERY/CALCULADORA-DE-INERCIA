from dash import html # Se importa dash 
import dash_bootstrap_components as dbc # Se importa los componentes deBootstrap 

# Se crea una variable que contenga: 
arriba = dbc.Container(

    [
        html.H2("Seleccione una figura geométrica:"), # Se le pone un titulo. 
        html.Hr(), # se le pone una división 
    ]
)

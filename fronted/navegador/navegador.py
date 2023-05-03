from dash import html # Se importa el HTML 
import dash_bootstrap_components as dbc # Se importan los componentes del Bootstrap

# Se genera una variable que contenga
navegador = dbc.Container(
    [
        html.H1("CALCULADORA DE INERCIAS"), # El titulo principal 
        html.Hr(), # una división 
    ]
)
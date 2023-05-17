from dash import html # importar dash 
import dash_bootstrap_components as dbc #importar los componentes del Bootstrap

# Se crea una variable que contenga: 

abajo = dbc.Container(
    [   dbc.Row(html.Div(id='resultadocalcular')),])
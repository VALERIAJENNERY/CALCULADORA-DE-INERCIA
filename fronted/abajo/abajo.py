from dash import html # importar dash 
import dash_bootstrap_components as dbc #importar los componentes del Bootstrap
from fronted.abajo.propiedades import propiedades # importar las propiedades geométricas 
from fronted.abajo.grafica import contenido

# Se crea una variable que contenga: 

abajo = dbc.Container(
    [
        dbc.Row( # Una fila 
            [
                dbc.Col(contenido, md=8, style ={'background-color':'#C88DDF', 'border': '1px solid purple'}), # Una columna con el nombre grafica 
                dbc.Col(propiedades, md=4, style ={'background-color':'#C88DDF', 'border': '1px solid purple'}),# Una columna con las propiedades geométricas
                
    ], 
        )
        
    ]
)
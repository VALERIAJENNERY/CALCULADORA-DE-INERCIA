from dash import html # importar dash 
import dash_bootstrap_components as dbc #importar los componentes del Bootstrap
from fronted.abajo.propiedades import propiedades # importar las propiedades geométricas 

# Se crea una variable que contenga: 

abajo = dbc.Container(
    [
        dbc.Row( # Una fila 
            [
                dbc.Col('GRAFICA', md=6, style ={'background-color':'pink'}), # Una columna con el nombre grafica 
                dbc.Col(propiedades, md=6, style ={'background-color':'pink'}),# Una columna con las propiedades geométricas
                
    ]
        )
        
    ]
)
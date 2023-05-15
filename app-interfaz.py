import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output,State

# Importar backend
from back.areas import a_rectangulo
# Importar frontend
from fronted.navegador.navegador import navegador
from fronted.arriba.arriba import arriba
from fronted.botones.botones import botones, aceptar
from fronted.datos.datos_rec import altura_rec,datos_rec
from fronted.datos.datos_cir import radio_cir,datos_cir
from fronted.datos.datos_semicir import radio_semicir, datos_semicir
from fronted.datos.datos_cuartocir import radio_cuartocir, datos_cuartocir
from fronted.datos.datos_arco import radio_arco,datos_arco
from fronted.datos.datos_trian import altura_trian,datos_trian
from fronted.abajo.abajo import abajo

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True)


app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(navegador, md=12, style={'background-color': 'white'}),
                
                dbc.Col('Valeria Hernandez - 20222579021', md=4,
                        style={'background-color': 'white', 
                               "font-family": "Arial Narrow", 
                               "color": "Black", 
                               "font-weight": "bold", 
                               "text-align": "center",
                               'border': '0.5px solid purple'}),
                
                dbc.Col('María Rojas - 20222579030', md=4,
                        style={'background-color': 'white',
                               "font-family": "Arial Narrow", 
                               "color": "Black", 
                               "font-weight": "bold", 
                               "text-align": "center",
                               'border': '0.5px solid purple'}),
                
                dbc.Col(arriba, md=12, style={'background-color': 'white'}),
                
                dbc.Col(botones, md=12, style={'background-color': 'white', 'margin-bottom': '10px'}),
                
                html.Hr(style={'display': 'none'}),
                
                dbc.Col(datos_rec, md=8, style={'background-color': 'white', 
                                                "font-family": "Arial Narrow", 
                                                "color": "Black", "font-weight": "bold", 
                                                "text-align": "center",
                                                'margin-bottom': '10px',

                                                }),
                
                html.Hr(style={'display': 'none'}),
                
                dbc.Col(datos_cir, md=8, style={'background-color': 'white', 
                                                "font-family": "Arial Narrow", 
                                                "color": "Black", "font-weight": "bold", 
                                                "text-align": "center",
                                                'margin-bottom': '10px',

                                                }),  
                
                html.Hr(style={'display': 'none'}),
                
                dbc.Col(datos_semicir, md=8, style={'background-color': 'white', 
                                                "font-family": "Arial Narrow", 
                                                "color": "Black", "font-weight": "bold", 
                                                "text-align": "center",
                                                'margin-bottom': '10px',
                                                }),
                
                html.Hr(style={'display': 'none'}),
                
                dbc.Col(datos_cuartocir, md=8, style={'background-color': 'white', 
                                                "font-family": "Arial Narrow", 
                                                "color": "Black", "font-weight": "bold", 
                                                "text-align": "center",
                                                'margin-bottom': '10px',
                                                }),
                
                html.Hr(style={'display': 'none'}),
                
                dbc.Col(datos_arco, md=8, style={'background-color': 'white', 
                                                "font-family": "Arial Narrow", 
                                                "color": "Black", "font-weight": "bold", 
                                                "text-align": "center",
                                                'margin-bottom': '10px',
                                                }),                

                html.Hr(style={'display': 'none'}),
                
                dbc.Col(datos_trian, md=8, style={'background-color': 'white', 
                                                "font-family": "Arial Narrow", 
                                                "color": "Black", "font-weight": "bold", 
                                                "text-align": "center",
                                                'margin-bottom': '10px',
                                                }),                

                html.Hr(style={'display': 'none'}),
                
                dbc.Col(aceptar, md=8, style={'background-color': 'white'}),
                
                dbc.Col(abajo, md=12, style={'background-color': '#C88DD'}),
                
            ], style={'justify-content': 'center'}
        )
    ]
)

# para que el botón me muestre los datos de entrada del rectangulo.

@app.callback(
    Output('resultado_rectangulo', 'children'),
    [Input('boton_rectangulo', 'n_clicks')],
    [State('resultado_rectangulo', 'children')],
)

def datos_rec(n_clicks, children):
    if n_clicks is None:
        return children
    if n_clicks % 2 == 1:
        return html.Div(
            id='resultado_rectangulo',
            children=[altura_rec],
        )
    else:
        return html.Div(id='resultado_rectangulo', children=[])
    
# para que el botón me muestre los datos de entrada del circulo.

@app.callback(
    Output('resultado_circulo', 'children'),
    [Input('boton_circulo', 'n_clicks')],
    [State('resultado_circulo', 'children')],
)

def datos_rec(n_clicks, children):
    if n_clicks is None:
        return children
    if n_clicks % 2 == 1:
        return html.Div(
            id='resultado_circulo',
            children=[radio_cir],
        )
    else:
        return html.Div(id='resultado_circulo', children=[])
    
# para que el botón me muestre los datos de entrada del semicirculo.

@app.callback(
    Output('resultado_semicirculo', 'children'),
    [Input('boton_semicirculo', 'n_clicks')],
    [State('resultado_semicirculo', 'children')],
)

def datos_rec(n_clicks, children):
    if n_clicks is None:
        return children
    if n_clicks % 2 == 1:
        return html.Div(
            id='resultado_semicirculo',
            children=[radio_semicir],
        )
    else:
        return html.Div(id='resultado_semicirculo', children=[])

 # para que el botón me muestre los datos de entrada del cuarto de circulo.

@app.callback(
    Output('resultado_cuartocirculo', 'children'),
    [Input('boton_cuartocirculo', 'n_clicks')],
    [State('resultado_cuartocirculo', 'children')],
)

def datos_rec(n_clicks, children):
    if n_clicks is None:
        return children
    if n_clicks % 2 == 1:
        return html.Div(
            id='resultado_cuartocirculo',
            children=[radio_cuartocir],
        )
    else:
        return html.Div(id='resultado_cuartocirculo', children=[])   

 # para que el botón me muestre los datos de entrada del arco.

@app.callback(
    Output('resultado_arco', 'children'),
    [Input('boton_arco', 'n_clicks')],
    [State('resultado_arco', 'children')],
)

def datos_rec(n_clicks, children):
    if n_clicks is None:
        return children
    if n_clicks % 2 == 1:
        return html.Div(
            id='resultado_arco',
            children=[radio_arco],
        )
    else:
        return html.Div(id='resultado_arco', children=[])
    
 # para que el botón me muestre los datos de entrada del arco.

@app.callback(
    Output('resultado_triangulo', 'children'),
    [Input('boton_triangulo', 'n_clicks')],
    [State('resultado_triangulo', 'children')],
)

def datos_rec(n_clicks, children):
    if n_clicks is None:
        return children
    if n_clicks % 2 == 1:
        return html.Div(
            id='resultado_triangulo',
            children=[altura_trian],
        )
    else:
        return html.Div(id='resultado_triangulo', children=[])
    
# para el funcionamiento 
@app.callback(
    Output('salida_altura_rec', 'children'),
    [Input('entrada_altura_rec', 'value'),
     Input('entrada_base_rec', 'value')]
)


def a_rectanguloDash(entrada_base_rec,entrada_altura_rec):

    area_rec = a_rectangulo(entrada_base_rec,entrada_altura_rec)

    return "El área del rectángulo es: ", area_rec, "m\xb2"

if __name__ == "__main__":
    app.run_server(debug=True)

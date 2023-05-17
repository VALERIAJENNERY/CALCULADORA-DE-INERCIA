import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output,State

# Importar backend
from BACK.areas import *
from BACK.centroide import*
from BACK.inercia import *
from BACK.graficas import *
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
from fronted.abajo.calculosRec import abajo_Rec
from fronted.abajo.calculosCir import abajo_Cir
from fronted.abajo.calculosSemicir import abajo_Semicir
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
    
# Para el funcionamiento de las areas
@app.callback(
    Output('salida_altura_rec', 'children'),
    [Input('entrada_base_rec', 'value'),
     Input('entrada_altura_rec', 'value')]
)


def a_rectanguloDash(entrada_base_rec,entrada_altura_rec):

    area_rec = a_rectangulo(entrada_base_rec,entrada_altura_rec)
    return "{:.2f} m\xb2".format(area_rec)
  
@app.callback(
    Output('salida_a_circulo', 'children'),
    [Input('entrada_circulo', 'value'),
    ]
)

def a_circuloDash(entrada_circulo):
    area_cir = a_circulo(entrada_circulo)
    return "{:.2f} m\xb2".format(area_cir)

@app.callback(
    Output('salida_a_semicirculo', 'children'),
    [Input('entrada_semicirculo', 'value'),
    ]
)

def a_semicirculoDash(entrada_semicirculo):
    area_semicir = a_semicirculo(entrada_semicirculo)
    return "{:.2f} m\xb2".format(area_semicir)

# Para el funcionamiento de los centroides 
@app.callback(
    Output('salida_cx_rec', 'children'),
    [Input('entrada_base_rec', 'value'),
     Input('entrada_altura_rec', 'value')]
)


def cx_rectanguloDash(entrada_base_rec,entrada_altura_rec):

    cx_rec = cx_rectangulo(entrada_base_rec,entrada_altura_rec)

    return "{:.2f} m".format(cx_rec)

@app.callback(
    Output('salida_cx_cir', 'children'),
    [Input('entrada_circulo', 'value'),
     ]
)
def cx_circuloDash(entrada_circulo):

    cx_cir = cx_circulo(entrada_circulo)

    return "{:.2f} m".format(cx_cir)

@app.callback(
    Output('salida_cx_semicir', 'children'),
    [Input('entrada_semicirculo', 'value'),
     ]
)
def cx_semicirculoDash(entrada_semicirculo):

    cx_semicir = cx_semicirculo(entrada_semicirculo)

    return "{:.2f} m".format(cx_semicir)

@app.callback(
    Output('salida_cy_rec', 'children'),
    [Input('entrada_base_rec', 'value'),
     Input('entrada_altura_rec', 'value')]
)
def cy_rectanguloDash(entrada_base_rec,entrada_altura_rec):

    cy_rec = cy_rectangulo(entrada_base_rec,entrada_altura_rec)

    return "{:.2f} m".format(cy_rec)

@app.callback(
    Output('salida_cy_cir', 'children'),
    [Input('entrada_circulo', 'value'),
     ]
)

def cy_circuloDash(entrada_circulo):

    cy_cir = cy_circulo(entrada_circulo)

    return "{:.2f} m".format(cy_cir)

@app.callback(
    Output('salida_cy_semicir', 'children'),
    [Input('entrada_semicirculo', 'value'),
     ]
)

def cy_semicirculoDash(entrada_semicirculo):

    cy_semicir = cy_semicirculo(entrada_semicirculo)

    return "{:.2f} m".format(cy_semicir)
# Para el funcionamiento de las inercias del rectangulo y la grafica
@app.callback(
    Output('salida_ix_rec', 'children'),
    [Input('entrada_base_rec', 'value'),
     Input('entrada_altura_rec', 'value')]
)
def ix_rectanguloDash(entrada_base_rec,entrada_altura_rec):

    ix_rec = ix_rectangulo(entrada_base_rec,entrada_altura_rec)

    return "{:.2f} m⁴".format(ix_rec)

@app.callback(
    Output('salida_ix_cir', 'children'),
    [Input('entrada_circulo', 'value'),
     ]
)
def ix_circuloDash(entrada_circulo):

    ix_cir = ix_circulo(entrada_circulo)

    return "{:.2f} m⁴".format(ix_cir)

@app.callback(
    Output('salida_ix_semicir', 'children'),
    [Input('entrada_semicirculo', 'value'),
     ]
)
def ix_semicirculoDash(entrada_semicirculo):

    ix_semicir = ix_semicirculo(entrada_semicirculo)

    return "{:.2f} m⁴".format(ix_semicir)

@app.callback(
    Output('salida_iy_rec', 'children'),
    [Input('entrada_base_rec', 'value'),
     Input('entrada_altura_rec', 'value')]
)
def iy_rectanguloDash(entrada_base_rec,entrada_altura_rec):

    iy_rec = iy_rectangulo(entrada_base_rec,entrada_altura_rec)

    return "{:.2f} m⁴".format(iy_rec)

@app.callback(
    Output('salida_iy_cir', 'children'),
    [Input('entrada_circulo', 'value'),
     ]
)
def iy_circuloDash(entrada_circulo):

    iy_cir = iy_circulo(entrada_circulo)

    return "{:.2f} m⁴".format(iy_cir)

@app.callback(
    Output('salida_iy_semicir', 'children'),
    [Input('entrada_semicirculo', 'value'),
     ]
)
def iy_semicirculoDash(entrada_semicirculo):

    iy_semicir = iy_semicirculo(entrada_semicirculo)

    return "{:.2f} m⁴".format(iy_semicir)

@app.callback(
    Output('salida_j_rec', 'children'),
    [Input('entrada_base_rec', 'value'),
     Input('entrada_altura_rec', 'value')]
)
def j_rectanguloDash(entrada_base_rec,entrada_altura_rec):

    j_rec = j_rectangulo(entrada_base_rec,entrada_altura_rec)

    return "{:.2f} m⁴".format(j_rec)

@app.callback(
    Output('salida_j_cir', 'children'),
    [Input('entrada_circulo', 'value'),
     ]
)
def j_circuloDash(entrada_circulo):

    j_cir = j_circulo(entrada_circulo)

    return "{:.2f} m⁴".format(j_cir)

@app.callback(
    Output('salida_j_semicir', 'children'),
    [Input('entrada_semicirculo', 'value'),
     ]
)
def j_semicirculoDash(entrada_semicirculo):

    j_semicir = j_semicirculo(entrada_semicirculo)

    return "{:.2f} m⁴".format(j_semicir)

@app.callback(
    Output('salida_grafica_rec', 'children'),
    [Input('entrada_base_rec', 'value'),
     Input('entrada_altura_rec', 'value')]
)
def grafica_rectanguloDash(entrada_base_rec,entrada_altura_rec):

    encoded_image= graficar_rectangulo(entrada_base_rec, entrada_altura_rec)

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))
    return html.Div([image_element])

@app.callback(
    Output('salida_grafica_cir', 'children'),
    [Input('entrada_circulo', 'value'),
     ]
)
def grafica_circuloDash(entrada_circulo):

    encoded_image= graficar_circulo(entrada_circulo)

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))
    return html.Div([image_element])

@app.callback(
    Output('salida_grafica_semicir', 'children'),
    [Input('entrada_semicirculo', 'value'),
     ]
)
def grafica_semicirculoDash(entrada_semicirculo):

    encoded_image= graficar_semicirculo(entrada_semicirculo)

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))
    return html.Div([image_element])
#para el botón calcular

@app.callback(
    Output('resultadocalcular', 'children'),
    [Input('calcular', 'n_clicks')],
    [State('boton_rectangulo', 'n_clicks'),
     State('boton_circulo', 'n_clicks'),
     State('boton_semicirculo', 'n_clicks'),
     State('boton_cuartocirculo', 'n_clicks'), 
     State('boton_arco', 'n_clicks'), 
     State('boton_triangulo', 'n_clicks')],
    prevent_initial_call=True
)
def mostrar_calculos(n_clicks_calcular, n_clicks_rectangulo, n_clicks_circulo, n_clicks_semicirculo,n_clicks_cuarto,n_clicks_arco, n_clicks_triangulo):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'calcular':
        if n_clicks_rectangulo and not n_clicks_circulo and not n_clicks_semicirculo and not n_clicks_cuarto and not n_clicks_arco and not n_clicks_triangulo:
            return abajo_Rec  # Resultado para el rectángulo
        elif n_clicks_circulo and not n_clicks_rectangulo and not n_clicks_semicirculo and not n_clicks_cuarto and not n_clicks_arco and not n_clicks_triangulo:
            return abajo_Cir  # Resultado para el círculo
        elif n_clicks_semicirculo and not n_clicks_rectangulo and not n_clicks_circulo and not n_clicks_cuarto and not n_clicks_arco and not n_clicks_triangulo:
            return abajo_Semicir  # Resultado para el semicírculo
        elif n_clicks_cuarto and not n_clicks_rectangulo and not n_clicks_circulo and not n_clicks_semicirculo and not n_clicks_arco and not n_clicks_triangulo:
            return 'mora'  # Resultado para el semicírculo
        elif n_clicks_arco and not n_clicks_rectangulo and not n_clicks_circulo and not n_clicks_semicirculo and not n_clicks_cuarto and not n_clicks_triangulo:
            return 'fresa'  # Resultado para el semicírcul       
        elif n_clicks_triangulo and not n_clicks_rectangulo and not n_clicks_circulo and not n_clicks_semicirculo and not n_clicks_cuarto and not n_clicks_arco:
            return 'mango'  # Resultado para el semicírcul       
        else:
            return ''

    return None


@app.callback(
    Output('boton_rectangulo', 'n_clicks'),
    [Input('calcular', 'n_clicks')],
    [State('boton_rectangulo', 'n_clicks'),
     State('boton_circulo', 'n_clicks'),
     State('boton_semicirculo', 'n_clicks'),
     State('boton_cuartocirculo', 'n_clicks'), 
     State('boton_arco', 'n_clicks'), 
     State('boton_triangulo', 'n_clicks')],
    prevent_initial_call=True
)
def reset_rectangulo(n_clicks_calcular, n_clicks_rectangulo, n_clicks_circulo, n_clicks_semicirculo, n_clicks_cuarto,n_clicks_arco,n_clicks_triangulo ):
    if n_clicks_calcular:
        return 0
    return n_clicks_rectangulo


@app.callback(
    Output('boton_circulo', 'n_clicks'),
    [Input('calcular', 'n_clicks')],
    [State('boton_rectangulo', 'n_clicks'),
     State('boton_circulo', 'n_clicks'),
     State('boton_semicirculo', 'n_clicks'),
     State('boton_cuartocirculo', 'n_clicks'), 
     State('boton_arco', 'n_clicks'), 
     State('boton_triangulo', 'n_clicks')],
    prevent_initial_call=True
)
def reset_circulo(n_clicks_calcular, n_clicks_rectangulo, n_clicks_circulo, n_clicks_semicirculo,n_clicks_cuarto,n_clicks_arco,n_clicks_triangulo ):
    if n_clicks_calcular:
        return 0
    return n_clicks_circulo


@app.callback(
    Output('boton_semicirculo', 'n_clicks'),
    [Input('calcular', 'n_clicks')],
    [State('boton_rectangulo', 'n_clicks'),
     State('boton_circulo', 'n_clicks'),
     State('boton_semicirculo', 'n_clicks'),
     State('boton_cuartocirculo', 'n_clicks'), 
     State('boton_arco', 'n_clicks'), 
     State('boton_triangulo', 'n_clicks')],
    prevent_initial_call=True
)
def reset_semicirculo(n_clicks_calcular, n_clicks_rectangulo, n_clicks_circulo, n_clicks_semicirculo,n_clicks_cuarto, n_clicks_arco, n_clicks_triangulo):
    if n_clicks_calcular:
        return 0
    return n_clicks_semicirculo

@app.callback(
    Output('boton_cuartocirculo', 'n_clicks'),
    [Input('calcular', 'n_clicks')],
    [State('boton_rectangulo', 'n_clicks'),
     State('boton_circulo', 'n_clicks'),
     State('boton_semicirculo', 'n_clicks'),
     State('boton_cuartocirculo', 'n_clicks'), 
     State('boton_arco', 'n_clicks'), 
     State('boton_triangulo', 'n_clicks')],
    prevent_initial_call=True
)
def reset_cuarto(n_clicks_calcular, n_clicks_rectangulo, n_clicks_circulo, n_clicks_semicirculo,n_clicks_cuarto,n_clicks_arco,n_clicks_triangulo):
    if n_clicks_calcular:
        return 0
    return n_clicks_cuarto

@app.callback(
    Output('boton_arco', 'n_clicks'),
    [Input('calcular', 'n_clicks')],
    [State('boton_rectangulo', 'n_clicks'),
     State('boton_circulo', 'n_clicks'),
     State('boton_semicirculo', 'n_clicks'),
     State('boton_cuartocirculo', 'n_clicks'), 
     State('boton_arco', 'n_clicks'), 
     State('boton_triangulo', 'n_clicks')],
    prevent_initial_call=True
)
def reset_arco(n_clicks_calcular, n_clicks_rectangulo, n_clicks_circulo, n_clicks_semicirculo,n_clicks_cuarto,n_clicks_arco,n_clicks_triangulo):
    if n_clicks_calcular:
        return 0
    return n_clicks_arco

@app.callback(
    Output('boton_triangulo', 'n_clicks'),
    [Input('calcular', 'n_clicks')],
    [State('boton_rectangulo', 'n_clicks'),
     State('boton_circulo', 'n_clicks'),
     State('boton_semicirculo', 'n_clicks'),
     State('boton_cuartocirculo', 'n_clicks'), 
     State('boton_arco', 'n_clicks'), 
     State('boton_triangulo', 'n_clicks')],
    prevent_initial_call=True
)
def reset_arco(n_clicks_calcular, n_clicks_rectangulo, n_clicks_circulo, n_clicks_semicirculo,n_clicks_cuarto,n_clicks_arco,n_clicks_triangulo):
    if n_clicks_calcular:
        return 0
    return n_clicks_triangulo
if __name__ == "__main__":
    app.run_server(debug=True)
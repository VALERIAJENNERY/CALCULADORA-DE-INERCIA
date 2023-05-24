import dash                                            # Importar la biblioteca Dash
from dash import html                                  # Importar el módulo html de Dash
import dash_bootstrap_components as dbc                # Importar componentes de Bootstrap para Dash
from dash.dependencies import Input, Output, State     # Importar clases Input, Output y State de Dash

# Importar backend
from BACK.areas import *                               # Importar todos los elementos del módulo 'areas'
from BACK.centroide import*                            # Importar todos los elementos del módulo 'centroide'
from BACK.inercia import *                              # Importar todos los elementos del módulo 'inercia'
from BACK.graficas import *                             # Importar todos los elementos del módulo 'graficas'

# Importar frontend
from fronted.navegador.navegador import navegador       # Importar la función 'navegador' del módulo 'navegador' en el paquete 'fronted'
from fronted.arriba.arriba import arriba                # Importar la función 'arriba' del módulo 'arriba' en el paquete 'fronted'
from fronted.botones.botones import botones, aceptar    # Importar las funciones 'botones' y 'aceptar' del módulo 'botones' en el paquete 'fronted'
from fronted.datos.datos_rec import altura_rec,datos_rec # Importar las funciones 'altura_rec' y 'datos_rec' del módulo 'datos_rec' en el paquete 'fronted'
from fronted.datos.datos_cir import radio_cir,datos_cir # Importar las funciones 'radio_cir' y 'datos_cir' del módulo 'datos_cir' en el paquete 'fronted'
from fronted.datos.datos_semicir import radio_semicir, datos_semicir  # Importar las funciones 'radio_semicir' y 'datos_semicir' del módulo 'datos_semicir' en el paquete 'fronted'
from fronted.datos.datos_cuartocir import radio_cuartocir, datos_cuartocir  # Importar las funciones 'radio_cuartocir' y 'datos_cuartocir' del módulo 'datos_cuartocir' en el paquete 'fronted'
from fronted.datos.datos_arco import radio_arco,datos_arco   # Importar las funciones 'radio_arco' y 'datos_arco' del módulo 'datos_arco' en el paquete 'fronted'
from fronted.datos.datos_trian import altura_trian,datos_trian  # Importar las funciones 'altura_trian' y 'datos_trian' del módulo 'datos_trian' en el paquete 'fronted'
from fronted.abajo.abajo import abajo                    # Importar la función 'abajo' del módulo 'abajo' en el paquete 'fronted'
from fronted.abajo.calculosRec import abajo_Rec          # Importar la función 'abajo_Rec' del módulo 'calculosRec' en el paquete 'fronted'
from fronted.abajo.calculosCir import abajo_Cir          # Importar la función 'abajo_Cir' del módulo 'calculosCir' en el paquete 'fronted'
from fronted.abajo.calculosSemicir import abajo_Semicir  # Importar la función 'abajo_Semicir' del módulo 'calculosSemicir' en el paquete 'fronted'
from fronted.abajo.calculosCuartocir import abajo_Cuartocir  # Importar la función 'abajo_Cuartocir' del módulo 'calculosCuartocir' en el paquete 'fronted'
from fronted.abajo.calculosSeccir import abajo_Seccir    # Importar la función 'abajo_Seccir' del módulo 'calculosSeccir' en el paquete 'fronted'
from fronted.abajo.calculosTri import abajo_tri          # Importar la función 'abajo_tri' del módulo 'calculosTri' en el paquete 'fronted'

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True)  # Crear una aplicación Dash

app.layout = dbc.Container( #Establece el diseño principal de la aplicación
    [
        dbc.Row(#Crea una columna en el diseño utilizando el componente dbc.Col.
            [
                # Columna para el componente 'navegador'
                dbc.Col(navegador, md=12, style={'background-color': 'white'}),

                # Columna con información de las integrantes
                dbc.Col('Valeria Hernandez - 20222579021', md=4,
                        style={'background-color': 'white', 
                               "font-family": "Arial Narrow", 
                               "color": "Black", 
                               "font-weight": "bold", 
                               "text-align": "center",
                               'border': '0.5px solid purple'}),

                # Columna con información de las integrantes
                dbc.Col('María Rojas - 20222579030', md=4,
                        style={'background-color': 'white',
                               "font-family": "Arial Narrow", 
                               "color": "Black", 
                               "font-weight": "bold", 
                               "text-align": "center",
                               'border': '0.5px solid purple'}),

                # Columna para el componente 'arriba'
                dbc.Col(arriba, md=12, style={'background-color': 'white'}),

                # Columna para el componente 'botones'
                dbc.Col(botones, md=12, style={'background-color': 'white', 'margin-bottom': '10px'}),

                # Separador invisible (línea horizontal)
                html.Hr(style={'display': 'none'}),

                # Columna para el componente 'datos_rec'
                dbc.Col(datos_rec, md=8, style={'background-color': 'white', 
                                                "font-family": "Arial Narrow", 
                                                "color": "Black", "font-weight": "bold", 
                                                "text-align": "center",
                                                'margin-bottom': '10px'}),

                # Separador invisible
                html.Hr(style={'display': 'none'}),

                # Columna para el componente 'datos_cir'
                dbc.Col(datos_cir, md=8, style={'background-color': 'white', 
                                                "font-family": "Arial Narrow", 
                                                "color": "Black", 
                                                "font-weight": "bold", 
                                                "text-align": "center",
                                                'margin-bottom': '10px'}),

                # Separador invisible
                html.Hr(style={'display': 'none'}),

                # Columna para el componente 'datos_semicir'
                dbc.Col(datos_semicir, md=8, style={'background-color': 'white', 
                                                    "font-family": "Arial Narrow", 
                                                    "color": "Black", 
                                                    "font-weight": "bold", 
                                                    "text-align": "center",
                                                    'margin-bottom': '10px'}),

                # Separador invisible
                html.Hr(style={'display': 'none'}),

                # Columna para el componente 'datos_cuartocir'
                dbc.Col(datos_cuartocir, md=8, style={'background-color': 'white', 
                                                        "font-family": "Arial Narrow", 
                                                        "color": "Black", 
                                                        "font-weight": "bold", 
                                                        "text-align": "center",
                                                        'margin-bottom': '10px'}),

                # Separador invisible
                html.Hr(style={'display': 'none'}),

                # Columna para el componente 'datos_arco'
                dbc.Col(datos_arco, md=8, style={'background-color': 'white', 
                                                    "font-family": "Arial Narrow", 
                                                    "color": "Black", 
                                                    "font-weight": "bold", 
                                                    "text-align": "center",
                                                    'margin-bottom': '10px'}),

                # Separador invisible
                html.Hr(style={'display': 'none'}),

                # Columna para el componente 'datos_trian'
                dbc.Col(datos_trian, md=8, style={'background-color': 'white', 
                                                    "font-family": "Arial Narrow", 
                                                    "color": "Black", 
                                                    "font-weight": "bold", 
                                                    "text-align": "center",
                                                    'margin-bottom': '10px'}),

                # Separador invisible
                html.Hr(style={'display': 'none'}),

                # Columna para el componente 'aceptar'
                dbc.Col(aceptar, md=8, style={'background-color': 'white'}),

                # Columna para el componente 'abajo'
                dbc.Col(abajo, md=12, style={'background-color': '#C88DD'}),

            ], style={'justify-content': 'center'}#Establece la alineación horizontal de los elementos dentro del contenedor en el centro.
        )
    ]
)

# para que el botón me muestre los datos de entrada del rectangulo.

@app.callback(
    Output('resultado_rectangulo', 'children'),  # Define la salida de la callback
    [Input('boton_rectangulo', 'n_clicks')],  # Define la entrada de la callback
    [State('resultado_rectangulo', 'children')]  # Define el estado inicial de la salida
)

def datos_rec(n_clicks, children):  # Define la función que se ejecutará en la callback
    if n_clicks is None:  # Comprueba si no se ha hecho clic en el botón
        return children  # Devuelve el estado actual de la salida
    if n_clicks % 2 == 1:  # Comprueba si el número de clics es impar
        return html.Div(  # Devuelve un contenedor Div con una lista de hijos
            id='resultado_rectangulo',  # Asigna un ID al contenedor Div
            children=[altura_rec],  # Agrega el componente altura_rec como hijo
        )
    else:  # Si el número de clics es par
        return html.Div(id='resultado_rectangulo', children=[])  # Devuelve un contenedor Div vacío

# para que el botón me muestre los datos de entrada del circulo.

@app.callback(
    Output('resultado_circulo', 'children'),  # Define la salida de la callback
    [Input('boton_circulo', 'n_clicks')],  # Define la entrada de la callback
    [State('resultado_circulo', 'children')]  # Define el estado inicial de la salida
)

def datos_rec(n_clicks, children):  # Define la función que se ejecutará en la callback
    if n_clicks is None:  # Comprueba si no se ha hecho clic en el botón
        return children  # Devuelve el estado actual de la salida
    if n_clicks % 2 == 1:  # Comprueba si el número de clics es impar
        return html.Div(  # Devuelve un contenedor Div con una lista de hijos
            id='resultado_circulo',  # Asigna un ID al contenedor Div
            children=[radio_cir],  # Agrega el componente radio_cir como hijo
        )
    else:  # Si el número de clics es par
        return html.Div(id='resultado_circulo', children=[])  # Devuelve un contenedor Div vacío

    
# para que el botón me muestre los datos de entrada del semicirculo.
@app.callback(
    Output('resultado_semicirculo', 'children'),  # Define la salida de la callback
    [Input('boton_semicirculo', 'n_clicks')],  # Define la entrada de la callback
    [State('resultado_semicirculo', 'children')]  # Define el estado inicial de la salida
)

def datos_rec(n_clicks, children):  # Define la función que se ejecutará en la callback
    if n_clicks is None:  # Comprueba si no se ha hecho clic en el botón
        return children  # Devuelve el estado actual de la salida
    if n_clicks % 2 == 1:  # Comprueba si el número de clics es impar
        return html.Div(  # Devuelve un contenedor Div con una lista de hijos
            id='resultado_semicirculo',  # Asigna un ID al contenedor Div
            children=[radio_semicir],  # Agrega el componente radio_semicir como hijo
        )
    else:  # Si el número de clics es par
        return html.Div(id='resultado_semicirculo', children=[])  # Devuelve un contenedor Div vacío


 # para que el botón me muestre los datos de entrada del cuarto de circulo.
@app.callback(
    Output('resultado_cuartocirculo', 'children'),  # Define la salida de la callback
    [Input('boton_cuartocirculo', 'n_clicks')],  # Define la entrada de la callback
    [State('resultado_cuartocirculo', 'children')]  # Define el estado inicial de la salida
)

def datos_rec(n_clicks, children):  # Define la función que se ejecutará en la callback
    if n_clicks is None:  # Comprueba si no se ha hecho clic en el botón
        return children  # Devuelve el estado actual de la salida
    if n_clicks % 2 == 1:  # Comprueba si el número de clics es impar
        return html.Div(  # Devuelve un contenedor Div con una lista de hijos
            id='resultado_cuartocirculo',  # Asigna un ID al contenedor Div
            children=[radio_cuartocir],  # Agrega el componente radio_cuartocir como hijo
        )
    else:  # Si el número de clics es par
        return html.Div(id='resultado_cuartocirculo', children=[])  # Devuelve un contenedor Div vacío


 # para que el botón me muestre los datos de entrada del arco.

@app.callback(
    Output('resultado_arco', 'children'),  # Define la salida de la callback
    [Input('boton_arco', 'n_clicks')],  # Define la entrada de la callback
    [State('resultado_arco', 'children')]  # Define el estado inicial de la salida
)

def datos_rec(n_clicks, children):  # Define la función que se ejecutará en la callback
    if n_clicks is None:  # Comprueba si no se ha hecho clic en el botón
        return children  # Devuelve el estado actual de la salida
    if n_clicks % 2 == 1:  # Comprueba si el número de clics es impar
        return html.Div(  # Devuelve un contenedor Div con una lista de hijos
            id='resultado_arco',  # Asigna un ID al contenedor Div
            children=[radio_arco],  # Agrega el componente radio_arco como hijo
        )
    else:  # Si el número de clics es par
        return html.Div(id='resultado_arco', children=[])  # Devuelve un contenedor Div vacío

    
 # para que el botón me muestre los datos de entrada del triangulo.

@app.callback(
    Output('resultado_triangulo', 'children'),  # Define la salida de la callback
    [Input('boton_triangulo', 'n_clicks')],  # Define la entrada de la callback
    [State('resultado_triangulo', 'children')]  # Define el estado inicial de la salida
)

def datos_rec(n_clicks, children):  # Define la función que se ejecutará en la callback
    if n_clicks is None:  # Comprueba si no se ha hecho clic en el botón
        return children  # Devuelve el estado actual de la salida
    if n_clicks % 2 == 1:  # Comprueba si el número de clics es impar
        return html.Div(  # Devuelve un contenedor Div con una lista de hijos
            id='resultado_triangulo',  # Asigna un ID al contenedor Div
            children=[altura_trian],  # Agrega el componente altura_trian como hijo
        )
    else:  # Si el número de clics es par
        return html.Div(id='resultado_triangulo', children=[])  # Devuelve un contenedor Div vacío

    
# Para el funcionamiento de las areas
@app.callback(
    Output('salida_altura_rec', 'children'),  # Define la salida de la callback
    [Input('entrada_base_rec', 'value'),  # Define la entrada de la callback
     Input('entrada_altura_rec', 'value')]
)

def a_rectanguloDash(entrada_base_rec, entrada_altura_rec):  # Define la función que se ejecutará en la callback
    area_rec = a_rectangulo(entrada_base_rec, entrada_altura_rec)  # Calcula el área del rectángulo
    return "{:.2f} m\xb2".format(area_rec)  # Devuelve el área formateada como cadena

@app.callback(
    Output('salida_a_circulo', 'children'),  # Define la salida de la callback
    [Input('entrada_circulo', 'value'),  # Define la entrada de la callback
    ]
)

def a_circuloDash(entrada_circulo):  # Define la función que se ejecutará en la callback
    area_cir = a_circulo(entrada_circulo)  # Calcula el área del círculo
    return "{:.2f} m\xb2".format(area_cir)  # Devuelve el área formateada como cadena

@app.callback(
    Output('salida_a_semicirculo', 'children'),  # Define la salida de la callback
    [Input('entrada_semicirculo', 'value'),  # Define la entrada de la callback
    ]
)

def a_semicirculoDash(entrada_semicirculo):  # Define la función que se ejecutará en la callback
    area_semicir = a_semicirculo(entrada_semicirculo)  # Calcula el área del semicírculo
    return "{:.2f} m\xb2".format(area_semicir)  # Devuelve el área formateada como cadena

@app.callback(
    Output('salida_a_cuartocirculo', 'children'),  # Define la salida de la callback
    [Input('entrada_cuartocirculo', 'value'),  # Define la entrada de la callback
    ]
)

def a_cuartodecirculoDash(entrada_cuartocirculo):  # Define la función que se ejecutará en la callback
    area_cuarcir = a_cuartodecirculo(entrada_cuartocirculo)  # Calcula el área del cuarto de círculo
    return "{:.2f} m\xb2".format(area_cuarcir)  # Devuelve el área formateada como cadena

@app.callback(
    Output('salida_a_sectorcirculo', 'children'),  # Define la salida de la callback
    [Input('entrada_radio_sector', 'value'),  # Define la entrada de la callback
     Input('entrada_angulo_sector', 'value')
    ]
)

def a_sectorcircularDash(entrada_radio_sector, entrada_angulo_sector):  # Define la función que se ejecutará en la callback
    area_seccir = a_sectorcircular(entrada_radio_sector, entrada_angulo_sector)  # Calcula el área del sector circular
    return "{:.2f} m\xb2".format(area_seccir)  # Devuelve el área formateada como cadena

@app.callback(
    Output('salida_a_tri', 'children'),  # Define la salida de la callback
    [Input('entrada_base_trian', 'value'),  # Define la entrada de la callback
     Input('entrada_altura_trian', 'value'),
     Input('entrada_a_trian', 'value')
    ]
)

def a_trianguloDash(entrada_base_trian, entrada_altura_trian, entrada_a_trian):  # Define la función que se ejecutará en la callback
    area_tri = a_triangulo(entrada_base_trian, entrada_altura_trian, entrada_a_trian)  # Calcula el área del triángulo
    return "{:.2f} m\xb2".format(area_tri)  # Devuelve el área formateada como cadena



# Para el funcionamiento de los centroides 
@app.callback(
    Output('salida_cx_rec', 'children'),  # Define la salida de la callback
    [Input('entrada_base_rec', 'value'),  # Define la entrada de la callback
     Input('entrada_altura_rec', 'value')]
)


def cx_rectanguloDash(entrada_base_rec, entrada_altura_rec):  # Define la función que se ejecutará en la callback
    cx_rec = cx_rectangulo(entrada_base_rec, entrada_altura_rec)  # Calcula el centro de masa del rectángulo
    return "{:.2f} m".format(cx_rec)  # Devuelve el centro de masa formateado como cadena

@app.callback(
    Output('salida_cx_cir', 'children'),  # Define la salida de la callback
    [Input('entrada_circulo', 'value'),  # Define la entrada de la callback
     ]
)
def cx_circuloDash(entrada_circulo):  # Define la función que se ejecutará en la callback
    cx_cir = cx_circulo(entrada_circulo)  # Calcula el centro de masa del círculo
    return "{:.2f} m".format(cx_cir)  # Devuelve el centro de masa formateado como cadena

@app.callback(
    Output('salida_cx_semicir', 'children'),  # Define la salida de la callback
    [Input('entrada_semicirculo', 'value'),  # Define la entrada de la callback
     ]
)
def cx_semicirculoDash(entrada_semicirculo):  # Define la función que se ejecutará en la callback
    cx_semicir = cx_semicirculo(entrada_semicirculo)  # Calcula el centro de masa del semicírculo
    return "{:.2f} m".format(cx_semicir)  # Devuelve el centro de masa formateado como cadena

@app.callback(
    Output('salida_cx_cuarcir', 'children'),  # Define la salida de la callback
    [Input('entrada_cuartocirculo', 'value'),  # Define la entrada de la callback
     ]
)
def cx_cuartocirculoDash(entrada_cuartocirculo):  # Define la función que se ejecutará en la callback
    cx_cuarcir = cx_cuartodecirculo(entrada_cuartocirculo)  # Calcula el centro de masa del cuarto de círculo
    return "{:.2f} m".format(cx_cuarcir)  # Devuelve el centro de masa formateado como cadena

@app.callback(
    Output('salida_cx_seccir', 'children'),  # Define la salida de la callback
    [Input('entrada_radio_sector', 'value'),  # Define la entrada de la callback
     Input('entrada_angulo_sector', 'value')
     ]
)
def cx_sectorcircularDash(entrada_radio_sector, entrada_angulo_sector):  # Define la función que se ejecutará en la callback
    cx_seccir = cx_sectorcircular(entrada_radio_sector, entrada_angulo_sector)  # Calcula el centro de masa del sector circular
    return "{:.2f} m".format(cx_seccir)  # Devuelve el centro de masa formateado como cadena

@app.callback(
    Output('salida_cx_tri', 'children'),  # Define la salida de la callback
    [Input('entrada_base_trian', 'value'),  # Define la entrada de la callback
     Input('entrada_altura_trian', 'value'),
     Input('entrada_a_trian', 'value')
    ]
)
def cx_trianguloDash(entrada_base_trian, entrada_altura_trian, entrada_a_trian):  # Define la función que se ejecutará en la callback
    cx_tri = cx_triangulo(entrada_base_trian, entrada_altura_trian, entrada_a_trian)  # Calcula el centro de masa del triángulo
    return "{:.2f} m\xb2".format(cx_tri)  # Devuelve el centro de masa formateado como cadena


#Para el funcionamiento de cy

@app.callback(
    Output('salida_cy_rec', 'children'),  # Define la salida de la callback
    [Input('entrada_base_rec', 'value'),  # Define la entrada de la callback
     Input('entrada_altura_rec', 'value')]
)
def cy_rectanguloDash(entrada_base_rec, entrada_altura_rec):  # Define la función que se ejecutará en la callback
    cy_rec = cy_rectangulo(entrada_base_rec, entrada_altura_rec)  # Calcula la coordenada y del centro de masa del rectángulo
    return "{:.2f} m".format(cy_rec)  # Devuelve la coordenada y formateada como cadena

@app.callback(
    Output('salida_cy_cir', 'children'),  # Define la salida de la callback
    [Input('entrada_circulo', 'value'),  # Define la entrada de la callback
     ]
)
def cy_circuloDash(entrada_circulo):  # Define la función que se ejecutará en la callback
    cy_cir = cy_circulo(entrada_circulo)  # Calcula la coordenada y del centro de masa del círculo
    return "{:.2f} m".format(cy_cir)  # Devuelve la coordenada y formateada como cadena

@app.callback(
    Output('salida_cy_semicir', 'children'),  # Define la salida de la callback
    [Input('entrada_semicirculo', 'value'),  # Define la entrada de la callback
     ]
)
def cy_semicirculoDash(entrada_semicirculo):  # Define la función que se ejecutará en la callback
    cy_semicir = cy_semicirculo(entrada_semicirculo)  # Calcula la coordenada y del centro de masa del semicírculo
    return "{:.2f} m".format(cy_semicir)  # Devuelve la coordenada y formateada como cadena

@app.callback(
    Output('salida_cy_cuarcir', 'children'),  # Define la salida de la callback
    [Input('entrada_cuartocirculo', 'value'),  # Define la entrada de la callback
     ]
)
def cy_cuartocirculoDash(entrada_cuartocirculo):  # Define la función que se ejecutará en la callback
    cy_cuarcir = cy_cuartodecirculo(entrada_cuartocirculo)  # Calcula la coordenada y del centro de masa del cuarto de círculo
    return "{:.2f} m".format(cy_cuarcir)  # Devuelve la coordenada y formateada como cadena

@app.callback(
    Output('salida_cy_seccir', 'children'),  # Define la salida de la callback
    [Input('entrada_radio_sector', 'value'),  # Define la entrada de la callback
     Input('entrada_angulo_sector', 'value')
     ]
)
def cy_sectorcircularDash(entrada_radio_sector, entrada_angulo_sector):  # Define la función que se ejecutará en la callback
    cy_seccir = cy_sectorcircular(entrada_radio_sector, entrada_angulo_sector)  # Calcula la coordenada y del centro de masa del sector circular
    return "{:.2f} m".format(cy_seccir)  # Devuelve la coordenada y formateada como cadena

@app.callback(
    Output('salida_cy_tri', 'children'),  # Define la salida de la callback
    [Input('entrada_base_trian', 'value'),  # Define la entrada de la callback
     Input('entrada_altura_trian', 'value'),
     Input('entrada_a_trian', 'value')
    ]
)
def cy_trianguloDash(entrada_base_trian, entrada_altura_trian, entrada_a_trian):  # Define la función que se ejecutará en la callback
    cy_tri = cy_triangulo(entrada_base_trian, entrada_altura_trian, entrada_a_trian)  # Calcula la coordenada y del centro de masa del triángulo
    return "{:.2f} m\xb2".format(cy_tri)  # Devuelve la coordenada y formateada como cadena

# Para el funcionamiento de las inercias x
@app.callback(
    Output('salida_ix_rec', 'children'),  # Define la salida de la callback
    [Input('entrada_base_rec', 'value'),  # Define la entrada de la callback
     Input('entrada_altura_rec', 'value')]
)
def ix_rectanguloDash(entrada_base_rec, entrada_altura_rec):  # Define la función que se ejecutará en la callback
    ix_rec = ix_rectangulo(entrada_base_rec, entrada_altura_rec)  # Calcula el momento de inercia del rectángulo
    return "{:.2f} m⁴".format(ix_rec)  # Devuelve el momento de inercia formateado como cadena

@app.callback(
    Output('salida_ix_cir', 'children'),  # Define la salida de la callback
    [Input('entrada_circulo', 'value'),  # Define la entrada de la callback
     ]
)
def ix_circuloDash(entrada_circulo):  # Define la función que se ejecutará en la callback
    ix_cir = ix_circulo(entrada_circulo)  # Calcula el momento de inercia del círculo
    return "{:.2f} m⁴".format(ix_cir)  # Devuelve el momento de inercia formateado como cadena

@app.callback(
    Output('salida_ix_semicir', 'children'),  # Define la salida de la callback
    [Input('entrada_semicirculo', 'value'),  # Define la entrada de la callback
     ]
)
def ix_semicirculoDash(entrada_semicirculo):  # Define la función que se ejecutará en la callback
    ix_semicir = ix_semicirculo(entrada_semicirculo)  # Calcula el momento de inercia del semicírculo
    return "{:.2f} m⁴".format(ix_semicir)  # Devuelve el momento de inercia formateado como cadena

@app.callback(
    Output('salida_ix_cuarcir', 'children'),  # Define la salida de la callback
    [Input('entrada_cuartocirculo', 'value'),  # Define la entrada de la callback
     ]
)
def ix_cuartocirculoDash(entrada_cuartocirculo):  # Define la función que se ejecutará en la callback
    ix_cuarcir = ix_cuartodecirculo(entrada_cuartocirculo)  # Calcula el momento de inercia del cuarto de círculo
    return "{:.2f} m⁴".format(ix_cuarcir)  # Devuelve el momento de inercia formateado como cadena

@app.callback(
    Output('salida_ix_seccir', 'children'),  # Define la salida de la callback
    [Input('entrada_radio_sector', 'value'),  # Define la entrada de la callback
     Input('entrada_angulo_sector', 'value')
     ]
)
def ix_sectorcircularDash(entrada_radio_sector, entrada_angulo_sector):  # Define la función que se ejecutará en la callback
    ix_seccir = ix_sectorcircular(entrada_radio_sector, entrada_angulo_sector)  # Calcula el momento de inercia del sector circular
    return "{:.2f} m".format(ix_seccir)  # Devuelve el momento de inercia formateado como cadena

@app.callback(
    Output('salida_ix_tri', 'children'),  # Define la salida de la callback
    [Input('entrada_base_trian', 'value'),  # Define la entrada de la callback
     Input('entrada_altura_trian', 'value'),
     Input('entrada_a_trian', 'value')
    ]
)
def ix_trianguloDash(entrada_base_trian, entrada_altura_trian, entrada_a_trian):  # Define la función que se ejecutará en la callback
    ix_tri = ix_triangulo(entrada_base_trian, entrada_altura_trian, entrada_a_trian)  # Calcula el momento de inercia del triángulo
    return "{:.2f} m\xb2".format(ix_tri)  # Devuelve el momento de inercia formateado como cadena

#Para el funcionamiento de las inercias y
@app.callback(
    Output('salida_iy_rec', 'children'),  # Define la salida de la callback
    [Input('entrada_base_rec', 'value'),  # Define la entrada de la callback
     Input('entrada_altura_rec', 'value')]
)
def iy_rectanguloDash(entrada_base_rec, entrada_altura_rec):  # Define la función que se ejecutará en la callback
    iy_rec = iy_rectangulo(entrada_base_rec, entrada_altura_rec)  # Calcula el momento de inercia respecto al eje y del rectángulo
    return "{:.2f} m⁴".format(iy_rec)  # Devuelve el momento de inercia formateado como cadena

@app.callback(
    Output('salida_iy_cir', 'children'),  # Define la salida de la callback
    [Input('entrada_circulo', 'value'),  # Define la entrada de la callback
     ]
)
def iy_circuloDash(entrada_circulo):  # Define la función que se ejecutará en la callback
    iy_cir = iy_circulo(entrada_circulo)  # Calcula el momento de inercia respecto al eje y del círculo
    return "{:.2f} m⁴".format(iy_cir)  # Devuelve el momento de inercia formateado como cadena

@app.callback(
    Output('salida_iy_semicir', 'children'),  # Define la salida de la callback
    [Input('entrada_semicirculo', 'value'),  # Define la entrada de la callback
     ]
)
def iy_semicirculoDash(entrada_semicirculo):  # Define la función que se ejecutará en la callback
    iy_semicir = iy_semicirculo(entrada_semicirculo)  # Calcula el momento de inercia respecto al eje y del semicírculo
    return "{:.2f} m⁴".format(iy_semicir)  # Devuelve el momento de inercia formateado como cadena

@app.callback(
    Output('salida_iy_cuarcir', 'children'),  # Define la salida de la callback
    [Input('entrada_cuartocirculo', 'value'),  # Define la entrada de la callback
     ]
)
def iy_cuartocirculoDash(entrada_cuartocirculo):  # Define la función que se ejecutará en la callback
    iy_cuarcir = iy_cuartodecirculo(entrada_cuartocirculo)  # Calcula el momento de inercia respecto al eje y del cuarto de círculo
    return "{:.2f} m⁴".format(iy_cuarcir)  # Devuelve el momento de inercia formateado como cadena

@app.callback(
    Output('salida_iy_seccir', 'children'),  # Define la salida de la callback
    [Input('entrada_radio_sector', 'value'),  # Define la entrada de la callback
     Input('entrada_angulo_sector', 'value')
     ]
)
def iy_sectorcircularDash(entrada_radio_sector, entrada_angulo_sector):  # Define la función que se ejecutará en la callback
    iy_seccir = iy_sectorcircular(entrada_radio_sector, entrada_angulo_sector)  # Calcula el momento de inercia respecto al eje y del sector circular
    return "{:.2f} m".format(iy_seccir)  # Devuelve el momento de inercia formateado como cadena

@app.callback(
    Output('salida_iy_tri', 'children'),  # Define la salida de la callback
    [Input('entrada_base_trian', 'value'),  # Define la entrada de la callback
     Input('entrada_altura_trian', 'value'),
     Input('entrada_a_trian', 'value')
    ]
)
def iy_trianguloDash(entrada_base_trian, entrada_altura_trian, entrada_a_trian):  # Define la función que se ejecutará en la callback
    iy_tri = iy_triangulo(entrada_base_trian, entrada_altura_trian, entrada_a_trian)  # Calcula el momento de inercia respecto al eje y del triángulo
    return "{:.2f} m\xb2".format(iy_tri)  # Devuelve el momento de inercia formateado como cadena

#Para el funcionamiento de j 

@app.callback(
    Output('salida_j_rec', 'children'),  # Define la salida de la callback
    [Input('entrada_base_rec', 'value'),  # Define la entrada de la callback
     Input('entrada_altura_rec', 'value')]
)
def j_rectanguloDash(entrada_base_rec, entrada_altura_rec):  # Define la función que se ejecutará en la callback
    j_rec = j_rectangulo(entrada_base_rec, entrada_altura_rec)  # Calcula la rigidez torsional del rectángulo
    return "{:.2f} m⁴".format(j_rec)  # Devuelve la rigidez torsional formateada como cadena

@app.callback(
    Output('salida_j_cir', 'children'),  # Define la salida de la callback
    [Input('entrada_circulo', 'value'),  # Define la entrada de la callback
     ]
)
def j_circuloDash(entrada_circulo):  # Define la función que se ejecutará en la callback
    j_cir = j_circulo(entrada_circulo)  # Calcula la rigidez torsional del círculo
    return "{:.2f} m⁴".format(j_cir)  # Devuelve la rigidez torsional formateada como cadena

@app.callback(
    Output('salida_j_semicir', 'children'),  # Define la salida de la callback
    [Input('entrada_semicirculo', 'value'),  # Define la entrada de la callback
     ]
)
def j_semicirculoDash(entrada_semicirculo):  # Define la función que se ejecutará en la callback
    j_semicir = j_semicirculo(entrada_semicirculo)  # Calcula la rigidez torsional del semicírculo
    return "{:.2f} m⁴".format(j_semicir)  # Devuelve la rigidez torsional formateada como cadena

@app.callback(
    Output('salida_j_cuarcir', 'children'),  # Define la salida de la callback
    [Input('entrada_cuartocirculo', 'value'),  # Define la entrada de la callback
     ]
)
def j_cuartocirculoDash(entrada_cuartocirculo):  # Define la función que se ejecutará en la callback
    j_cuarcir = j_cuartodecirculo(entrada_cuartocirculo)  # Calcula la rigidez torsional del cuarto de círculo
    return "{:.2f} m⁴".format(j_cuarcir)  # Devuelve la rigidez torsional formateada como cadena

@app.callback(
    Output('salida_j_seccir', 'children'),  # Define la salida de la callback
    [Input('entrada_radio_sector', 'value'),  # Define la entrada de la callback
     Input('entrada_angulo_sector', 'value')
     ]
)
def j_sectorcircularDash(entrada_radio_sector, entrada_angulo_sector):  # Define la función que se ejecutará en la callback
    j_seccir = j_sectorcircular(entrada_radio_sector, entrada_angulo_sector)  # Calcula la rigidez torsional del sector circular
    return "{:.2f} m".format(j_seccir)  # Devuelve la rigidez torsional formateada como cadena

@app.callback(
    Output('salida_j_tri', 'children'),  # Define la salida de la callback
    [Input('entrada_base_trian', 'value'),  # Define la entrada de la callback
     Input('entrada_altura_trian', 'value'),
     Input('entrada_a_trian', 'value')
    ]
)
def j_trianguloDash(entrada_base_trian, entrada_altura_trian, entrada_a_trian):  # Define la función que se ejecutará en la callback
    j_tri = j_triangulo(entrada_base_trian, entrada_altura_trian, entrada_a_trian)  # Calcula la rigidez torsional del triángulo
    return "{:.2f} m\xb2".format(j_tri)  # Devuelve la rigidez torsional formateada como cadena


#Para el funcionamiento de las graficas
@app.callback(
    Output('salida_grafica_rec', 'children'),  # Define la salida de la callback
    [Input('entrada_base_rec', 'value'),  # Define la entrada de la callback
     Input('entrada_altura_rec', 'value')]
)
def grafica_rectanguloDash(entrada_base_rec, entrada_altura_rec):  # Define la función que se ejecutará en la callback
    encoded_image = graficar_rectangulo(entrada_base_rec, entrada_altura_rec)  # Genera la imagen del rectángulo
    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))  # Crea un elemento HTML de imagen con la imagen generada
    return html.Div([image_element])  # Devuelve el elemento HTML de la imagen dentro de un contenedor Div

@app.callback(
    Output('salida_grafica_cir', 'children'),  # Define la salida de la callback
    [Input('entrada_circulo', 'value'),  # Define la entrada de la callback
     ]
)
def grafica_circuloDash(entrada_circulo):  # Define la función que se ejecutará en la callback
    encoded_image = graficar_circulo(entrada_circulo)  # Genera la imagen del círculo
    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))  # Crea un elemento HTML de imagen con la imagen generada
    return html.Div([image_element])  # Devuelve el elemento HTML de la imagen dentro de un contenedor Div

@app.callback(
    Output('salida_grafica_semicir', 'children'),  # Define la salida de la callback
    [Input('entrada_semicirculo', 'value'),  # Define la entrada de la callback
     ]
)
def grafica_semicirculoDash(entrada_semicirculo):  # Define la función que se ejecutará en la callback
    encoded_image = graficar_semicirculo(entrada_semicirculo)  # Genera la imagen del semicírculo
    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))  # Crea un elemento HTML de imagen con la imagen generada
    return html.Div([image_element])  # Devuelve el elemento HTML de la imagen dentro de un contenedor Div

@app.callback(
    Output('salida_grafica_cuarcir', 'children'),  # Define la salida de la callback
    [Input('entrada_cuartocirculo', 'value'),  # Define la entrada de la callback
     ]
)
def grafica_cuartocirculoDash(entrada_cuartocirculo):  # Define la función que se ejecutará en la callback
    encoded_image = graficar_cuarto_circulo(entrada_cuartocirculo)  # Genera la imagen del cuarto de círculo
    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))  # Crea un elemento HTML de imagen con la imagen generada
    return html.Div([image_element])  # Devuelve el elemento HTML de la imagen dentro de un contenedor Div

@app.callback(
    Output('salida_grafica_seccir', 'children'),  # Define la salida de la callback
    [Input('entrada_radio_sector', 'value'),  # Define la entrada de la callback
     Input('entrada_angulo_sector', 'value')
     ]
)
def graficar_sectorDash(entrada_radio_sector, entrada_angulo_sector):  # Define la función que se ejecutará en la callback
    encoded_image = graficar_sector(entrada_radio_sector, entrada_angulo_sector)  # Genera la imagen del sector circular
    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))  # Crea un elemento HTML de imagen con la imagen generada
    return html.Div([image_element])  # Devuelve el elemento HTML de la imagen dentro de un contenedor Div

@app.callback(
    Output('salida_grafica_tri', 'children'),  # Define la salida de la callback
    [Input('entrada_base_trian', 'value'),  # Define la entrada de la callback
     Input('entrada_altura_trian', 'value'),
     Input('entrada_a_trian', 'value')
    ]
)
def graficar_trianguloDash(entrada_base_trian, entrada_altura_trian, entrada_a_trian):  # Define la función que se ejecutará en la callback
    encoded_image = graficar_triangulo(entrada_base_trian, entrada_altura_trian, entrada_a_trian)  # Genera la imagen del triángulo
    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))  # Crea un elemento HTML de imagen con la imagen generada
    return html.Div([image_element])  # Devuelve el elemento HTML de la imagen dentro de un contenedor Div

#para el botón calcular

@app.callback(
    Output('resultadocalcular', 'children'),  # Define la salida de la callback
    [Input('calcular', 'n_clicks')],  # Define la entrada de la callback
    [State('boton_rectangulo', 'n_clicks'),#definir las entradas de estado (State) en una callback. Estas entradas de estado representan el número de clics en los botones correspondientes. 
     State('boton_circulo', 'n_clicks'),
     State('boton_semicirculo', 'n_clicks'),
     State('boton_cuartocirculo', 'n_clicks'), 
     State('boton_arco', 'n_clicks'), 
     State('boton_triangulo', 'n_clicks')],
    prevent_initial_call=True
)
def mostrar_calculos(n_clicks_calcular, n_clicks_rectangulo, n_clicks_circulo, n_clicks_semicirculo, n_clicks_cuarto, n_clicks_arco, n_clicks_triangulo):  # Define la función que se ejecutará en la callback
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
            return abajo_Cuartocir  # Resultado para el cuarto de círculo
        elif n_clicks_arco and not n_clicks_rectangulo and not n_clicks_circulo and not n_clicks_semicirculo and not n_clicks_cuarto and not n_clicks_triangulo:
            return abajo_Seccir  # Resultado para el sector circular
        elif n_clicks_triangulo and not n_clicks_rectangulo and not n_clicks_circulo and not n_clicks_semicirculo and not n_clicks_cuarto and not n_clicks_arco:
            return abajo_tri  # Resultado para el triángulo
        else:
            return ''

    return None#devuelve None como resultado de la función en una callback.



@app.callback(
    Output('boton_rectangulo', 'n_clicks'),  # Salida: contador de clics del botón "rectángulo"
    [Input('calcular', 'n_clicks')],  # Entrada: clics del botón "calcular"
    [  # Estados: valores actuales de los contadores de clics de varios botones
        State('boton_rectangulo', 'n_clicks'),
        State('boton_circulo', 'n_clicks'),
        State('boton_semicirculo', 'n_clicks'),
        State('boton_cuartocirculo', 'n_clicks'),
        State('boton_arco', 'n_clicks'),
        State('boton_triangulo', 'n_clicks')
    ],
    prevent_initial_call=True  # Evitar activación durante la carga inicial
)
def reset_rectangulo(n_clicks_calcular, n_clicks_rectangulo, n_clicks_circulo, n_clicks_semicirculo, n_clicks_cuarto, n_clicks_arco, n_clicks_triangulo):
    if n_clicks_calcular:  # Verificar si se ha hecho clic en el botón "calcular"
        return 0  # Reiniciar el contador de clics del botón "rectángulo"
    return n_clicks_rectangulo  # Devolver el valor actual del contador de clics del botón "rectángulo"
@app.callback(
    Output('boton_circulo', 'n_clicks'),  # Salida: contador de clics del botón "círculo"
    [Input('calcular', 'n_clicks')],  # Entrada: clics del botón "calcular"
    [  # Estados: valores actuales de los contadores de clics de varios botones
        State('boton_rectangulo', 'n_clicks'),
        State('boton_circulo', 'n_clicks'),
        State('boton_semicirculo', 'n_clicks'),
        State('boton_cuartocirculo', 'n_clicks'),
        State('boton_arco', 'n_clicks'),
        State('boton_triangulo', 'n_clicks')
    ],
    prevent_initial_call=True  # Evitar activación durante la carga inicial
)
def reset_circulo(n_clicks_calcular, n_clicks_rectangulo, n_clicks_circulo, n_clicks_semicirculo, n_clicks_cuarto, n_clicks_arco, n_clicks_triangulo):
    if n_clicks_calcular:  # Verificar si se ha hecho clic en el botón "calcular"
        return 0  # Reiniciar el contador de clics del botón "círculo"
    return n_clicks_circulo  # Devolver el valor actual del contador de clics del botón "círculo"

@app.callback(
    Output('boton_semicirculo', 'n_clicks'),  # Salida: contador de clics del botón "semicírculo"
    [Input('calcular', 'n_clicks')],  # Entrada: clics del botón "calcular"
    [  # Estados: valores actuales de los contadores de clics de varios botones
        State('boton_rectangulo', 'n_clicks'),
        State('boton_circulo', 'n_clicks'),
        State('boton_semicirculo', 'n_clicks'),
        State('boton_cuartocirculo', 'n_clicks'),
        State('boton_arco', 'n_clicks'),
        State('boton_triangulo', 'n_clicks')
    ],
    prevent_initial_call=True  # Evitar activación durante la carga inicial
)
def reset_semicirculo(n_clicks_calcular, n_clicks_rectangulo, n_clicks_circulo, n_clicks_semicirculo, n_clicks_cuarto, n_clicks_arco, n_clicks_triangulo):
    if n_clicks_calcular:  # Verificar si se ha hecho clic en el botón "calcular"
        return 0  # Reiniciar el contador de clics del botón "semicírculo"
    return n_clicks_semicirculo  # Devolver el valor actual del contador de clics del botón "semicírculo"
@app.callback(
    Output('boton_cuartocirculo', 'n_clicks'),  # Salida: contador de clics del botón "cuartocirculo"
    [Input('calcular', 'n_clicks')],  # Entrada: clics del botón "calcular"
    [  # Estados: valores actuales de los contadores de clics de varios botones
        State('boton_rectangulo', 'n_clicks'),
        State('boton_circulo', 'n_clicks'),
        State('boton_semicirculo', 'n_clicks'),
        State('boton_cuartocirculo', 'n_clicks'),
        State('boton_arco', 'n_clicks'),
        State('boton_triangulo', 'n_clicks')
    ],
    prevent_initial_call=True  # Evitar activación durante la carga inicial
)
def reset_cuarto(n_clicks_calcular, n_clicks_rectangulo, n_clicks_circulo, n_clicks_semicirculo, n_clicks_cuarto, n_clicks_arco, n_clicks_triangulo):
    if n_clicks_calcular:  # Verificar si se ha hecho clic en el botón "calcular"
        return 0  # Reiniciar el contador de clics del botón "cuartocirculo"
    return n_clicks_cuarto  # Devolver el valor actual del contador de clics del botón "cuartocirculo"
@app.callback(
    Output('boton_arco', 'n_clicks'),  # Salida: contador de clics del botón "arco"
    [Input('calcular', 'n_clicks')],  # Entrada: clics del botón "calcular"
    [  # Estados: valores actuales de los contadores de clics de varios botones
        State('boton_rectangulo', 'n_clicks'),
        State('boton_circulo', 'n_clicks'),
        State('boton_semicirculo', 'n_clicks'),
        State('boton_cuartocirculo', 'n_clicks'),
        State('boton_arco', 'n_clicks'),
        State('boton_triangulo', 'n_clicks')
    ],
    prevent_initial_call=True  # Evitar activación durante la carga inicial
)
def reset_arco(n_clicks_calcular, n_clicks_rectangulo, n_clicks_circulo, n_clicks_semicirculo, n_clicks_cuarto, n_clicks_arco, n_clicks_triangulo):
    if n_clicks_calcular:  # Verificar si se ha hecho clic en el botón "calcular"
        return 0  # Reiniciar el contador de clics del botón "arco"
    return n_clicks_arco  # Devolver el valor actual del contador de clics del botón "arco"

@app.callback(
    Output('boton_triangulo', 'n_clicks'),  # Salida: contador de clics del botón "triangulo"
    [Input('calcular', 'n_clicks')],  # Entrada: clics del botón "calcular"
    [  # Estados: valores actuales de los contadores de clics de varios botones
        State('boton_rectangulo', 'n_clicks'),
        State('boton_circulo', 'n_clicks'),
        State('boton_semicirculo', 'n_clicks'),
        State('boton_cuartocirculo', 'n_clicks'),
        State('boton_arco', 'n_clicks'),
        State('boton_triangulo', 'n_clicks')
    ],
    prevent_initial_call=True  # Evitar activación durante la carga inicial
)
def reset_arco(n_clicks_calcular, n_clicks_rectangulo, n_clicks_circulo, n_clicks_semicirculo, n_clicks_cuarto, n_clicks_arco, n_clicks_triangulo):
    if n_clicks_calcular:  # Verificar si se ha hecho clic en el botón "calcular"
        return 0  # Reiniciar el contador de clics del botón "triangulo"
    return n_clicks_triangulo  # Devolver el valor actual del contador de clics del botón "triangulo"

if __name__ == "__main__":
    app.run_server(debug=True)  # Ejecutar la aplicación en modo de depuración

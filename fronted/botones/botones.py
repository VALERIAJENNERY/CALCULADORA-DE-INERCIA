from dash import html  # Importar Html de dash
import dash_bootstrap_components as dbc  # importar componentes de Bootstrap

# Se crea una variable que contenga los botones, para cada boton se adjunta una imagen respectiva que indica las medidas de entrada
#Para cada boton se ajusta del estilo. como color, alineación y demás.
botones = html.Div([
    dbc.Button(
        id='boton_rectangulo',
        children=[
            html.Img(src='assets/imagenes/rectangulo.jpg', height='180px', className='me-1',  style={'padding': '0px'}),
            html.Div('Rectangulo', style={'display': 'flex', 'flex-direction': 'column'}),
            html.Span(id="rectangulo_output", style={"verticalAlign": "middle"}),
        ],
        color="danger",
        className="me-1"
    ),  # Botón Rectángulo

    dbc.Button(
        id='boton_circulo',
        children=[
            html.Img(src='assets/imagenes/circulo.jpg', height='180px', className='me-1', style={'padding': '0px'}),
            html.Div('Circulo', style={'display': 'flex', 'flex-direction': 'column'}),
            html.Span(id="circulo_output", style={"verticalAlign": "middle"}),
        ],
        color="danger",
        className="me-1"
    ),  # Botón Círculo

    dbc.Button(
        id='boton_semicirculo',
        children=[
            html.Img(src='assets/imagenes/semicirculo.jpg', height='180px', className='me-1', style={'padding': '0px'}),
            html.Div('Semicirculo', style={'display': 'flex', 'flex-direction': 'column'}),
            html.Span(id="semicirculo_output", style={"verticalAlign": "middle"}),
        ],
        color="danger",
        className="me-1"
    ),  # Botón Semicírculo

    dbc.Button(
        id='boton_cuartocirculo',
        children=[
            html.Img(src='assets/imagenes/cuartocirculo.jpg', height='180px', className='me-1',style={'padding': '0px'}),
            html.Div('Cuarto de circulo', style={'display': 'flex', 'flex-direction': 'column'}),
            html.Span(id="cuartocirculo_output", style={"verticalAlign": "middle"}),
        ],
        color="danger",
        className="me-1"
    ),  # Botón Cuarto de Círculo

    dbc.Button(
        id='boton_arco',
        children=[
            html.Img(src='assets/imagenes/arco.jpg', height='180px', className='me-1',style={'padding': '0px'}),
            html.Div('Arco', style={'display': 'flex', 'flex-direction': 'column'}),
            html.Span(id="arco_output", style={"verticalAlign": "middle"}),
        ],
        color="danger",
        className="me-1"
    ),  # Botón Arco

    dbc.Button(
        id='boton_triangulo',
        children=[
            html.Img(src='assets/imagenes/triangulo.jpg', height='180px', className='me-1',style={'padding': '0px'}),
            html.Div('Triangulo', style={'display': 'flex', 'flex-direction': 'column'}),
            html.Span(id="triangulo_output", style={"verticalAlign": "middle"}),
        ],
        color="danger",
        className="me-1"
    ),  # Botón Triángulo

    html.Hr(),  # Separador horizontal
], style={'display': 'flex', 'justify-content': 'center'})

# Se genera una variable que contenga el botón que nos ayudará a calcular
aceptar = html.Div([
    html.Div(
        dbc.Button(
            id="calcular",
            children=["Calcular", html.Span(id="calcular_output", style={"verticalAlign": "middle"})],
            outline=True,
            color="danger",
            className="me-1"
        ),
        style={"text-align": "center"},
    ),
    html.Hr(),
])

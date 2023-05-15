import dash_bootstrap_components as dbc # importar los componentes de Bootstrap 
from dash import html # Importar Html de dash 

# Se crea una variable que contenga los botones 
botones = html.Div([
    dbc.Button(
        id='boton_rectangulo',
        children=[
            
            html.Img(src='https://dr282zn36sxxg.cloudfront.net/datastreams/f-d%3A59b48c7f8d5cc42cb3c9137492d5cf83e57311e9b7af61655ebe5a4a%2BIMAGE_TINY%2BIMAGE_TINY.1', height='50px', className='me-1',  style={'background-color': 'pink', 'padding': '5px'}),
            html.Div('Rectangulo', style={'display': 'flex', 'flex-direction': 'column'}),
            html.Span(id="rectangulo_output", style={"verticalAlign": "middle"}),
        ],
        color="danger",
        className="me-1"
    ), 
    dbc.Button(
        id='boton_circulo',
        children=[
            html.Img(src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Circle_%28transparent%29.svg/800px-Circle_%28transparent%29.svg.png', height='50px', className='me-1', style={'background-color': 'pink', 'padding': '5px'}),
            html.Div('Circulo', style={'display': 'flex', 'flex-direction': 'column'}),
            html.Span(id="circulo_output", style={"verticalAlign": "middle"}),
        ],
        color="danger",
        className="me-1"
    ),
    dbc.Button(
        id='boton_semicirculo',
        children=[
            html.Img(src='https://prints.ultracoloringpages.com/ffa9ecad4a496e654ba8f9aef3c56e8b.png', height='50px', className='me-1', style={'background-color': 'pink', 'padding': '5px'}),
            html.Div('Semicirculo', style={'display': 'flex', 'flex-direction': 'column'}),
            html.Span(id="semicirculo_output", style={"verticalAlign": "middle"}),
        ],
        color="danger",
        className="me-1"
    ),
    dbc.Button(
        id='boton_cuartocirculo',
        children=[
            html.Img(src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRN4XhlAFvq0-i6oqxe_pT5saVn9HpyDLXxiw&usqp=CAU', height='50px', className='me-1',style={'background-color': 'pink', 'padding': '5px'}),
            html.Div('Cuarto de circulo', style={'display': 'flex', 'flex-direction': 'column'}),
            html.Span(id="cuartocirculo_output", style={"verticalAlign": "middle"}),
        ],
        color="danger",
        className="me-1"
    ),
    dbc.Button(
        id='boton_arco',
        children=[
            html.Img(src='https://matematicasies.com/local/cache-vignettes/L166xH164/maties_2018_b-5ac62.png?1572662933', height='50px', className='me-1',style={'background-color': 'pink', 'padding': '5px'}),
            html.Div('Arco', style={'display': 'flex', 'flex-direction': 'column'}),
            html.Span(id="arco_output", style={"verticalAlign": "middle"}),
            
        ],
        color="danger",
        className="me-1"
    ),
    dbc.Button(
        id='boton_triangulo',
        children=[
            html.Img(src='https://w7.pngwing.com/pngs/640/706/png-transparent-drawing-penrose-triangle-art-triangle-element-angle-rectangle-triangle.png', height='50px', className='me-1',style={'background-color': 'pink', 'padding': '5px'}),
            html.Div('Triangulo', style={'display': 'flex', 'flex-direction': 'column'}),
            html.Span(id="triangulo_output", style={"verticalAlign": "middle"}),
            
        ],
        color="danger",
        className="me-1"
    ), html.Hr(), # agregamos un separador horizontal
 
], style={'display': 'flex', 'justify-content': 'center'},),
   
    
    # Se genera una variable que contenga el  botón que nos ayudará a calcular
    
aceptar = html.Div(
    [
        html.Div(
            dbc.Button(
                id="calcular",  # Agregar el ID
                children=["Calcular", html.Span(id="calcular_output", style={"verticalAlign": "middle"})],
                outline=True,
                color="danger",
                className="me-1"
            ),
            
            style={"text-align": "center"},
        ),
        html.Hr(),
    ]
)
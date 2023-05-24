import dash_bootstrap_components as dbc  # Importa el módulo dash_bootstrap_components con alias dbc
from dash import html  # Importa la clase html del módulo dash
from dash import dcc  # Importa la clase dcc del módulo dash

altura_trian = dbc.Row(  # Crea una fila utilizando el componente Row de dbc y asigna el resultado a la variable 
    [
        html.Div(  # Crea un div utilizando el componente Div de html
            [
                html.Label('Altura (H): ', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                dcc.Input(id='entrada_altura_trian', value=5, type='number', style={'display': 'inline-block','margin-bottom': '10px'}),  # Crea un campo de entrada numérico utilizando el componente Input de dcc con estilo
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                html.Hr(style={'display': 'none'})  # Crea un separador horizontal utilizando el componente Hr de html con estilo
            ]
        ),
        html.Div(  # Crea otro div utilizando el componente Div de html
            [
                html.Label('Base (B): ', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                dcc.Input(id='entrada_base_trian', value=5, type='number', style={'display': 'inline-block','margin-bottom': '10px'}),  # Crea un campo de entrada numérico utilizando el componente Input de dcc con estilo
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                html.Hr(style={'display': 'none'})  # Crea un separador horizontal utilizando el componente Hr de html con estilo
            ]
        ),
        html.Div(  # Crea otro div utilizando el componente Div de html
            [
                html.Label('Distancia (A): ', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                dcc.Input(id='entrada_a_trian', value=5, type='number', style={'display': 'inline-block','margin-bottom': '10px'}),  # Crea un campo de entrada numérico utilizando el componente Input de dcc con estilo
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                html.Hr(style={'display': 'none'})  # Crea un separador horizontal utilizando el componente Hr de html con estilo
            ]
        ),        

    ]
)

datos_trian = html.Div(id="resultado_triangulo", children=[]),  # Crea un div vacío con un ID específico y asigna el resultado a la variable datos_trian
area_tri = html.Div(html.Label(id='salida_a_tri'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el area del triangulo
cx_tri = html.Div(html.Label(id='salida_cx_tri'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el centroide en x del triangulo
cy_tri = html.Div(html.Label(id='salida_cy_tri'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el centroide en y del triangulo
ix_tri = html.Div(html.Label(id='salida_ix_tri'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el momento de inercia en x del triangfulo
iy_tri = html.Div(html.Label(id='salida_iy_tri'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el momento de inercia en y del tyriangulo
j_tri = html.Div(html.Label(id='salida_j_tri'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para la constante torsional del triangulo

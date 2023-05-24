import dash_bootstrap_components as dbc  # Importa el módulo dash_bootstrap_components con alias dbc
from dash import html  # Importa la clase html del módulo dash
from dash import dcc  # Importa la clase dcc del módulo dash

altura_rec = dbc.Row(  # Crea una fila utilizando el componente Row de dbc y asigna el resultado a la variable altura_rec
    [
        html.Div(  # Crea un div utilizando el componente Div de html
            [
                html.Label('Altura (H): ', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                dcc.Input(id='entrada_altura_rec', value=5, type='number', style={'display': 'inline-block','margin-bottom': '10px'}),  # Crea un campo de entrada numérico utilizando el componente Input de dcc con estilo
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                html.Hr(style={'display': 'none'})  # Crea un separador horizontal utilizando el componente Hr de html con estilo
            ]
        ),
        html.Div(  # Crea un div utilizando el componente Div de html
            [
                html.Label('Base (B): ', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                dcc.Input(id='entrada_base_rec', value=5.5, type='number', style={'display': 'inline-block','margin-bottom': '10px'}),  # Crea un campo de entrada numérico utilizando el componente Input de dcc con estilo
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                html.Hr(style={'display': 'none'})  # Crea un separador horizontal utilizando el componente Hr de html con estilo
            ]
        ),
        
        
    ]
)

datos_rec = html.Div(id="resultado_rectangulo", children=[]),  # Crea un div vacío con un ID específico y asigna el resultado a la variable datos_rec
area_rectangulo = html.Div(html.Label(id='salida_altura_rec'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el area
cx_rectangulo = html.Div(html.Label(id='salida_cx_rec'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el centroide en x
cy_rectangulo = html.Div(html.Label(id='salida_cy_rec'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el centroide en y
ix_rectangulo = html.Div(html.Label(id='salida_ix_rec'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el momento de inercia en x
iy_rectangulo = html.Div(html.Label(id='salida_iy_rec'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el momento de inercia en y
j_rectangulo = html.Div(html.Label(id='salida_j_rec'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para j

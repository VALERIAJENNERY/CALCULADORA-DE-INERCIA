import dash_bootstrap_components as dbc  # Importa el módulo dash_bootstrap_components con alias dbc
from dash import html  # Importa la clase html del módulo dash
from dash import dcc  # Importa la clase dcc del módulo dash

radio_cuartocir = dbc.Row(  # Crea una fila utilizando el componente Row de dbc y asigna el resultado a la variable radio_cuartocir
    [
        html.Div(  # Crea un div utilizando el componente Div de html
            [
                html.Label('Radio (R): ', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                dcc.Input(id='entrada_cuartocirculo', value=5, type='number', style={'display': 'inline-block'}),  # Crea un campo de entrada numérico utilizando el componente Input de dcc con estilo
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                html.Hr(style={'display': 'none'})  # Crea un separador horizontal utilizando el componente Hr de html con estilo
            ]
        ),
        
    ]
)

datos_cuartocir = html.Div(id="resultado_cuartocirculo", children=[])  # Crea un div vacío con un ID específico y asigna el resultado a la variable datos_cuartocir
area_cuartocirculo = html.Div(html.Label(id='salida_a_cuartocirculo'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el area
cx_cuartocirculo = html.Div(html.Label(id='salida_cx_cuarcir'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el centroide en x
cy_cuartocirculo = html.Div(html.Label(id='salida_cy_cuarcir'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el centroide en y
ix_cuartocirculo = html.Div(html.Label(id='salida_ix_cuarcir'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el momento de inercia en x
iy_cuartocirculo = html.Div(html.Label(id='salida_iy_cuarcir'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el momento de inercia en y
j_cuartocirculo = html.Div(html.Label(id='salida_j_cuarcir'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para j

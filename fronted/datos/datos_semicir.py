import dash_bootstrap_components as dbc  # Importa el módulo dash_bootstrap_components con alias dbc
from dash import html  # Importa la clase html del módulo dash
from dash import dcc  # Importa la clase dcc del módulo dash

radio_semicir = dbc.Row(  # Crea una fila utilizando el componente Row de dbc y asigna el resultado a la variable 
    [
        html.Div(  # Crea un div utilizando el componente Div de html
            [
                html.Label('Radio (R): ', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                dcc.Input(id='entrada_semicirculo', value=5, type='number', style={'display': 'inline-block'}),  # Crea un campo de entrada numérico utilizando el componente Input de dcc con estilo
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                html.Hr(style={'display': 'none'})  # Crea un separador horizontal utilizando el componente Hr de html con estilo
            ]
        ),
        
        html.Label(id='salida_semicirculo')  # Crea una etiqueta de texto con un ID específico
    ]
)

datos_semicir = html.Div(id="resultado_semicirculo", children=[]),  # Crea un div vacío con un ID específico y asigna el resultado a la variable datos_semicir
area_semicirculo = html.Div(html.Label(id='salida_a_semicirculo'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el area
cx_semicirculo = html.Div(html.Label(id='salida_cx_semicir'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el centroide en x
cy_semicirculo = html.Div(html.Label(id='salida_cy_semicir'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el centroide en y
ix_semicirculo = html.Div(html.Label(id='salida_ix_semicir'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el momento de inerica en x
iy_semicirculo = html.Div(html.Label(id='salida_iy_semicir'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el momento de inercia en y
j_semicirculo = html.Div(html.Label(id='salida_j_semicir'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para j

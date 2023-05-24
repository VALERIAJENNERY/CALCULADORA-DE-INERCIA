import dash_bootstrap_components as dbc  # Importa el módulo dash_bootstrap_components con alias dbc
from dash import html  # Importa la clase html del módulo dash
from dash import dcc  # Importa la clase dcc del módulo dash

radio_arco = dbc.Row(  # Crea una fila utilizando el componente Row de dbc y asigna el resultado a la variable 
    [
        html.Div(  # Crea un div utilizando el componente Div de html
            [
                html.Label('Radio (R): ', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                dcc.Input(id='entrada_radio_sector', value=5, type='number', style={'display': 'inline-block','margin-bottom': '10px'}),  # Crea un campo de entrada numérico utilizando el componente Input de dcc con estilo
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                html.Hr(style={'display': 'none'})  # Crea un separador horizontal utilizando el componente Hr de html con estilo
            ]
        ),
        
        html.Div(  # Crea un div utilizando el componente Div de html
            [
                html.Label('Ángulo (α): ', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                dcc.Input(id='entrada_angulo_sector', value=30, type='number', style={'display': 'inline-block','margin-bottom': '10px'}),  # Crea un campo de entrada numérico utilizando el componente Input de dcc con estilo
                html.Label('grados', style={'display': 'inline-block', 'width': '120px'}),  # Crea una etiqueta de texto utilizando el componente Label de html con estilo
                html.Hr(style={'display': 'none'})  # Crea un separador horizontal utilizando el componente Hr de html con estilo
            ]
        ),

    ]
)

datos_arco = html.Div(id="resultado_arco", children=[])  # Crea un div vacío con un ID específico y asigna el resultado a la variable datos_arco
area_seccirculo = html.Div(html.Label(id='salida_a_sectorcirculo'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el area
cx_seccirculo = html.Div(html.Label(id='salida_cx_seccir'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el centroide en x
cy_seccirculo = html.Div(html.Label(id='salida_cy_seccir'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el centroide en y
ix_seccirculo = html.Div(html.Label(id='salida_ix_seccir'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el momento de inercia en x
iy_seccirculo = html.Div(html.Label(id='salida_iy_seccir'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para el momento de inercia en y
j_seccirculo = html.Div(html.Label(id='salida_j_seccir'))  # Crea un div con una etiqueta de texto y un ID específico y asigna el resultado a la variable para j

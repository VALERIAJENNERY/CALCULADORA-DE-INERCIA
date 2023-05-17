import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

radio_cir = dbc.Row(
    [
        html.Div(
            [
                html.Label('Radio (R): ', style={'display': 'inline-block', 'width': '120px'}),
                dcc.Input(id='entrada_circulo', value=5, type='number', style={'display': 'inline-block'}),
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),
                html.Hr(style={'display': 'none'})
            ]
        ),
        
        html.Label(id='salida_circulo')
    ]
)

datos_cir = html.Div(id="resultado_circulo",children=[],)


area_circulo=html.Div(html.Label(id='salida_a_circulo'))
cx_circulo=html.Div(html.Label(id='salida_cx_cir'))
cy_circulo=html.Div(html.Label(id='salida_cy_cir'))
ix_circulo=html.Div(html.Label(id='salida_ix_cir'))
iy_circulo=html.Div(html.Label(id='salida_iy_cir'))
j_circulo=html.Div(html.Label(id='salida_j_cir'))
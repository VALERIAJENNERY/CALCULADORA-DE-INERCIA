import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

radio_semicir = dbc.Row(
    [
        html.Div(
            [
                html.Label('Radio (R): ', style={'display': 'inline-block', 'width': '120px'}),
                dcc.Input(id='entrada_semicirculo', value=5, type='number', style={'display': 'inline-block'}),
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),
                html.Hr(style={'display': 'none'})
            ]
        ),
        
        html.Label(id='salida_semicirculo')
    ]
)

datos_semicir = html.Div(id="resultado_semicirculo",children=[],)

area_semicirculo=html.Div(html.Label(id='salida_a_semicirculo'))
cx_semicirculo=html.Div(html.Label(id='salida_cx_semicir'))
cy_semicirculo=html.Div(html.Label(id='salida_cy_semicir'))
ix_semicirculo=html.Div(html.Label(id='salida_ix_semicir'))
iy_semicirculo=html.Div(html.Label(id='salida_iy_semicir'))
j_semicirculo=html.Div(html.Label(id='salida_j_semicir'))
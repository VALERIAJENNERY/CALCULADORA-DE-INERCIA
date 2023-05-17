import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

radio_cuartocir = dbc.Row(
    [
        html.Div(
            [
                html.Label('Radio (R): ', style={'display': 'inline-block', 'width': '120px'}),
                dcc.Input(id='entrada_cuartocirculo', value=5, type='number', style={'display': 'inline-block'}),
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),
                html.Hr(style={'display': 'none'})
            ]
        ),
        
    ]
)

datos_cuartocir = html.Div(id="resultado_cuartocirculo",children=[],)
area_cuartocirculo=html.Div(html.Label(id='salida_a_cuartocirculo'))
cx_cuartocirculo=html.Div(html.Label(id='salida_cx_cuarcir'))
cy_cuartocirculo=html.Div(html.Label(id='salida_cy_cuarcir'))
ix_cuartocirculo=html.Div(html.Label(id='salida_ix_cuarcir'))
iy_cuartocirculo=html.Div(html.Label(id='salida_iy_cuarcir'))
j_cuartocirculo=html.Div(html.Label(id='salida_j_cuarcir'))
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

radio_arco = dbc.Row(
    [
        html.Div(
            [
                html.Label('Radio (R): ', style={'display': 'inline-block', 'width': '120px'}),
                dcc.Input(id='entrada_radio_sector', value=5, type='number', style={'display': 'inline-block','margin-bottom': '10px'}),
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),
                html.Hr(style={'display': 'none'})
            ]
        ),
        
        html.Div(
            [
                html.Label('Ángulo (α): ', style={'display': 'inline-block', 'width': '120px'}),
                dcc.Input(id='entrada_angulo_sector', value=30, type='number', style={'display': 'inline-block','margin-bottom': '10px'}),
                html.Label('grados', style={'display': 'inline-block', 'width': '120px'}),
                html.Hr(style={'display': 'none'})
            ]
        ),
        

    ]
)

datos_arco = html.Div(id="resultado_arco",children=[],)
area_seccirculo=html.Div(html.Label(id='salida_a_sectorcirculo'))
cx_seccirculo=html.Div(html.Label(id='salida_cx_seccir'))
cy_seccirculo=html.Div(html.Label(id='salida_cy_seccir'))
ix_seccirculo=html.Div(html.Label(id='salida_ix_seccir'))
iy_seccirculo=html.Div(html.Label(id='salida_iy_seccir'))
j_seccirculo=html.Div(html.Label(id='salida_j_seccir'))
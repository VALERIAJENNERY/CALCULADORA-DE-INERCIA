import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

altura_rec = dbc.Row(
    [
        html.Div(
            [
                html.Label('Altura (H): ', style={'display': 'inline-block', 'width': '120px'}),
                dcc.Input(id='entrada_altura_rec', value=5, type='number', style={'display': 'inline-block','margin-bottom': '10px'}),
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),
                html.Hr(style={'display': 'none'})
            ]
        ),
        html.Div(
            [
                html.Label('Base (B): ', style={'display': 'inline-block', 'width': '120px'}),
                dcc.Input(id='entrada_base_rec', value=5.5, type='number', style={'display': 'inline-block','margin-bottom': '10px'}),
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),
                html.Hr(style={'display': 'none'})
            ]
        ),
        
        
    ]
)

datos_rec = html.Div(id="resultado_rectangulo",children=[],)

area_rectangulo=html.Div(html.Label(id='salida_altura_rec'))
cx_rectangulo=html.Div(html.Label(id='salida_cx_rec'))
cy_rectangulo=html.Div(html.Label(id='salida_cy_rec'))
ix_rectangulo=html.Div(html.Label(id='salida_ix_rec'))
iy_rectangulo=html.Div(html.Label(id='salida_iy_rec'))
j_rectangulo=html.Div(html.Label(id='salida_j_rec'))
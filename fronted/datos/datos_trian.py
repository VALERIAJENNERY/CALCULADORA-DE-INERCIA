import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

altura_trian = dbc.Row(
    [
        html.Div(
            [
                html.Label('Altura (H): ', style={'display': 'inline-block', 'width': '120px'}),
                dcc.Input(id='entrada_altura_trian', value=5, type='number', style={'display': 'inline-block','margin-bottom': '10px'}),
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),
                html.Hr(style={'display': 'none'})
            ]
        ),
        html.Div(
            [
                html.Label('Base (B): ', style={'display': 'inline-block', 'width': '120px'}),
                dcc.Input(id='entrada_base_trian', value=5, type='number', style={'display': 'inline-block','margin-bottom': '10px'}),
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),
                html.Hr(style={'display': 'none'})
            ]
        ),
        html.Div(
            [
                html.Label('Distancia (A): ', style={'display': 'inline-block', 'width': '120px'}),
                dcc.Input(id='entrada_a_trian', value=5, type='number', style={'display': 'inline-block','margin-bottom': '10px'}),
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),
                html.Hr(style={'display': 'none'})
            ]
        ),        

    ]
)

datos_trian = html.Div(id="resultado_triangulo",children=[],)
area_tri=html.Div(html.Label(id='salida_a_tri'))
cx_tri=html.Div(html.Label(id='salida_cx_tri'))
cy_tri=html.Div(html.Label(id='salida_cy_tri'))
ix_tri=html.Div(html.Label(id='salida_ix_tri'))
iy_tri=html.Div(html.Label(id='salida_iy_tri'))
j_tri=html.Div(html.Label(id='salida_j_tri'))
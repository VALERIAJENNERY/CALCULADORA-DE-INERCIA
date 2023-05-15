import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

radio_cir = dbc.Row(
    [
        html.Div(
            [
                html.Label('Radio (r): ', style={'display': 'inline-block', 'width': '120px'}),
                dcc.Input(id='entrada_circulo', value=5, type='number', style={'display': 'inline-block'}),
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),
                html.Hr(style={'display': 'none'})
            ]
        ),
        
        html.Label(id='salida_circulo')
    ]
)

datos_cir = html.Div(id="resultado_circulo",children=[],)
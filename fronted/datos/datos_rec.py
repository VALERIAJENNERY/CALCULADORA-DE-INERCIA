import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

altura_rec = dbc.Row(
    [
        html.Div(
            [
                html.Label('Altura (h) en metros: ', style={'display': 'inline-block', 'width': '120px'}),
                dcc.Input(id='entrada_altura_rec', value=5, type='number', style={'display': 'inline-block'}),
                html.Hr(style={'display': 'none'})
            ]
        ),
        html.Div(
            [
                html.Label('Base (b) en metros: ', style={'display': 'inline-block', 'width': '120px'}),
                dcc.Input(id='entrada_base_rec', value=5, type='number', style={'display': 'inline-block'}),
                html.Hr(style={'display': 'none'})
            ]
        ),
        html.Label(id='salida_altura_rec')
    ]
)

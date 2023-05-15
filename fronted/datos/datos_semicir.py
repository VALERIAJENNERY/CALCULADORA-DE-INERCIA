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
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

radio_arco = dbc.Row(
    [
        html.Div(
            [
                html.Label('Radio (r): ', style={'display': 'inline-block', 'width': '120px'}),
                dcc.Input(id='entrada_radio_sector', value=5, type='number', style={'display': 'inline-block','margin-bottom': '10px'}),
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),
                html.Hr(style={'display': 'none'})
            ]
        ),
        
        html.Div(
            [
                html.Label('Ángulo (α): ', style={'display': 'inline-block', 'width': '120px'}),
                dcc.Input(id='entrada_angulo_sector', value=5, type='number', style={'display': 'inline-block','margin-bottom': '10px'}),
                html.Label('m', style={'display': 'inline-block', 'width': '120px'}),
                html.Hr(style={'display': 'none'})
            ]
        ),
        
        html.Label(id='salida_arco')
    ]
)

datos_arco = html.Div(id="resultado_arco",children=[],)
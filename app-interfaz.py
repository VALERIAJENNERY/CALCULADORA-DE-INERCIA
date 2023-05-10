import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Importar backend
from BACK.areas import a_rectangulo
# Importar frontend
from fronted.navegador.navegador import navegador
from fronted.arriba.arriba import arriba
from fronted.botones.botones import botones, aceptar
from fronted.datos.datos_rec import altura_rec
from fronted.abajo.abajo import abajo

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(navegador, md=12, style={'background-color': 'white'}),
                dbc.Col('Valeria Hernandez - 20222579021', md=4,
                        style={'background-color': '#C88DDF', "font-family": "Arial Narrow", "color": "Black", "font-weight": "bold", "text-align": "center"}),
                dbc.Col('María Rojas - 20222579030', md=4,
                        style={'background-color': '#C88DDF', "font-family": "Arial Narrow", "color": "Black", "font-weight": "bold", "text-align": "center"}),
                dbc.Col(arriba, md=12, style={'background-color': 'white'}),
                dbc.Col(botones, md=12, style={'background-color': 'white'}),
                html.Hr(style={'display': 'none'}),
                html.Hr(style={'display': 'none'}),
                dbc.Col(altura_rec, md=8, style={'background-color': 'white'}),
                html.Hr(style={'display': 'none'}),
                dbc.Col(aceptar, md=8, style={'background-color': 'white'}),
                dbc.Col(abajo, md=12, style={'background-color': '#C88DDF'}),
            ], style={'justify-content': 'center'}
        )
    ]
)


@app.callback(
    Output('salida_altura_rec', 'children'),
    [Input('entrada_altura_rec', 'value'),
     Input('entrada_base_rec', 'value')]
)
def a_rectanguloDash(entrada_base_rec, entrada_altura_rec):

    area_rec = a_rectangulo(entrada_base_rec, entrada_altura_rec)

    return "El área del rectángulo es: ", area_rec, "m\xb2"

if __name__ == "__main__":
    app.run_server(debug=True)

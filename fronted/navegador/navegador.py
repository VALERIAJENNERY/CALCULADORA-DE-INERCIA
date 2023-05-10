from dash import html # Se importa el HTML 
import dash_bootstrap_components as dbc # Se importan los componentes del Bootstrap

# Se genera una variable que contenga
navegador = dbc.Container(
    [
        html.Div([
            html.Img(src="https://previews.123rf.com/images/illizium/illizium1606/illizium160600020/58843416-tecnolog%C3%ADa-de-alta-tecnolog%C3%ADa-digital-y-la-ingenier%C3%ADa-la-tecnolog%C3%ADa-digital-de-telecomunicaciones.jpg", style={"float": "left", "margin-right": "10px", "width": "80px"}),
            html.Div([
                html.H1("CALCULADORA DE INERCIAS", style={"font-family": "Arial Narrow", "color": "purple", "font-weight": "bold"}),
            ], className="contenedor"),
          
        ], style={"display": "flex", "align-items": "center", "justify-content": "center"},
            ),
          html.Hr(style={"border": "5px solid purple"})
    ]
)

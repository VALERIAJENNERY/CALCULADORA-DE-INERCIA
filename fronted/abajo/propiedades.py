from dash import html # importar dash 
import dash_bootstrap_components as dbc #importar los componentes del Bootstrap

# Se crea una lista de propiedades 
propiedades = html.Div(
    [  # Se crea una fila.
        dbc.Row(
            [
                dbc.Col('PROPIEDADES GEOMÉTRICAS', md=12, style ={'background-color':'pink'}) # Se crea una columna con el titulo.
            ],
        ), 
        # Se crea una fila.
        dbc.Row(
            [
                dbc.Col(html.Div("Inercía (Iy)")), # Se crea una colmna con el nombre d ela propiedad
                dbc.Col(html.Div("16")), # Se crea una columna dondé se mostrarán los resultados
                dbc.Col(html.Div("m\xb4")), # Se crea una columna donde aparecerá las unidades
            ],
            align="center", # Se alinean los titulos en el centro 
        ),
        # Se crea una fila.
         dbc.Row(
            [
                dbc.Col(html.Div("Inercía (Ix)")), # Se crea una colmna con el nombre d ela propiedad
                dbc.Col(html.Div("16")), # Se crea una columna dondé se mostrarán los resultados
                dbc.Col(html.Div("m\xb4")), #  Se crea una columna donde aparecerá las unidades
            ],
            align="center",# Se alinean los titulos en el centro 
        ),
         # Se crea una fila.
          dbc.Row(
            [
                dbc.Col(html.Div("Área (A)")), # Se crea una colmna con el nombre d ela propiedad
                dbc.Col(html.Div("16")), # Se crea una columna dondé se mostrarán los resultados
                dbc.Col(html.Div("m\xb2")), #  Se crea una columna donde aparecerá las unidades
            ],
            align="center",# Se alinean los titulos en el centro
        ),
          # Se crea una fila.
           dbc.Row(
            [
                dbc.Col(html.Div("Centroide x (Cx)")), # Se crea una colmna con el nombre de la propiedad
                dbc.Col(html.Div("16")),# Se crea una columna dondé se mostrarán los resultados
                dbc.Col(html.Div("m")),#  Se crea una columna donde aparecerá las unidades 
            ],
            align="center", # Se alinean los titulos en el centro
        ),
           # Se crea una fila.
            dbc.Row(
            [
                dbc.Col(html.Div("Centroide y (Cy)")), # Se crea una colmna con el nombre de la propiedad
                dbc.Col(html.Div("16")), # Se crea una columna dondé se mostrarán los resultados
                dbc.Col(html.Div("m")),#  Se crea una columna donde aparecerá las unidades
            ],
            align="center",# Se alinean los titulos en el centro
        ),
            # Se crea una fila.
             dbc.Row(
            [
                dbc.Col(html.Div("Constante Torsional (J)")), # Se crea una colmna con el nombre de la propiedad
                dbc.Col(html.Div("16")), # Se crea una columna dondé se mostrarán los resultados
                dbc.Col(html.Div("m\xb4")),#  Se crea una columna donde aparecerá las unidades
            ],
            align="center",# Se alinean los titulos en el centro
        ),
        
    ],
    className="pad-row",
)


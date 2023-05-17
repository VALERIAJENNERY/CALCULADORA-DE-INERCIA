from dash import html # importar dash 
import dash_bootstrap_components as dbc #importar los componentes del Bootstrap
from fronted.datos.datos_rec import *

# Se crea una lista de propiedades para rectangulo

row1_rec = html.Tr([html.Td("Inercía (Iy)"), html.Td(iy_rectangulo)])
row2_rec = html.Tr([html.Td("Inercía (Ix)"), html.Td(ix_rectangulo)])
row3_rec = html.Tr([html.Td("Área (A)"), html.Td(area_rectangulo)])
row4_rec = html.Tr([html.Td("Centroide x (Cx)"), html.Td(cx_rectangulo)])
row5_rec = html.Tr([html.Td("Centroide y (Cy)"), html.Td(cy_rectangulo)])
row6_rec = html.Tr([html.Td("Constante Torsional (J)"), html.Td(j_rectangulo)])

table_body_rec = [html.Tbody([row1_rec, row2_rec, row3_rec, row4_rec,row5_rec,row6_rec])]

table_rec = dbc.Table( table_body_rec, bordered=True,
    style={'background-color': 'white', 
                               "font-family": "Arial Narrow", 
                               "color": "purple", 
                               "font-weight": "bold", 
                               "text-align": "center",
                               'border': '0.5px solid purple'}
)
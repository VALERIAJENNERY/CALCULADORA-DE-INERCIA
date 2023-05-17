from dash import html # importar dash 
import dash_bootstrap_components as dbc #importar los componentes del Bootstrap
from fronted.datos.datos_rec import *
from fronted.datos.datos_cir import *
from fronted.datos.datos_semicir import *
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

#se crea una lista de propiedades para el circulo
row1_cir = html.Tr([html.Td("Inercía (Iy)"), html.Td(iy_circulo)])
row2_cir = html.Tr([html.Td("Inercía (Ix)"), html.Td(ix_circulo)])
row3_cir = html.Tr([html.Td("Área (A)"), html.Td(area_circulo)])
row4_cir = html.Tr([html.Td("Centroide x (Cx)"), html.Td(cx_circulo)])
row5_cir = html.Tr([html.Td("Centroide y (Cy)"), html.Td(cy_circulo)])
row6_cir = html.Tr([html.Td("Constante Torsional (J)"), html.Td(j_circulo)])

table_body_cir = [html.Tbody([row1_cir, row2_cir, row3_cir, row4_cir,row5_cir,row6_cir])]

table_cir = dbc.Table( table_body_cir, bordered=True,
    style={'background-color': 'white', 
                               "font-family": "Arial Narrow", 
                               "color": "purple", 
                               "font-weight": "bold", 
                               "text-align": "center",
                               'border': '0.5px solid purple'}
)

#se crea una lista de propiedades para el semicirculo
row1_semicir = html.Tr([html.Td("Inercía (Iy)"), html.Td(iy_semicirculo)])
row2_semicir = html.Tr([html.Td("Inercía (Ix)"), html.Td(ix_semicirculo)])
row3_semicir = html.Tr([html.Td("Área (A)"), html.Td(area_semicirculo)])
row4_semicir = html.Tr([html.Td("Centroide x (Cx)"), html.Td(cx_semicirculo)])
row5_semicir = html.Tr([html.Td("Centroide y (Cy)"), html.Td(cy_semicirculo)])
row6_semicir = html.Tr([html.Td("Constante Torsional (J)"), html.Td(j_semicirculo)])

table_body_semicir = [html.Tbody([row1_semicir, row2_semicir, row3_semicir, row4_semicir,row5_semicir,row6_semicir])]

table_semicir = dbc.Table( table_body_semicir, bordered=True,
    style={'background-color': 'white', 
                               "font-family": "Arial Narrow", 
                               "color": "purple", 
                               "font-weight": "bold", 
                               "text-align": "center",
                               'border': '0.5px solid purple'}
)
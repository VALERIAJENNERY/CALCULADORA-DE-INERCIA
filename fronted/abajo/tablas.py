from dash import html  # Importar el módulo html de Dash
import dash_bootstrap_components as dbc  # Importar componentes de Bootstrap para Dash
from fronted.datos.datos_rec import *  # Importar datos de rectángulo
from fronted.datos.datos_cir import *  # Importar datos de círculo
from fronted.datos.datos_semicir import *  # Importar datos de semicírculo
from fronted.datos.datos_cuartocir import *  # Importar datos de cuarto de círculo
from fronted.datos.datos_arco import *  # Importar datos de arco
from fronted.datos.datos_trian import *  # Importar datos de triángulo

# Se crea una lista de propiedades para rectangulo: momento de inercia en x y y, area, centroides, y j

row1_rec = html.Tr([html.Td("Inercía (Iy)"), html.Td(iy_rectangulo)]) 
row2_rec = html.Tr([html.Td("Inercía (Ix)"), html.Td(ix_rectangulo)])
row3_rec = html.Tr([html.Td("Área (A)"), html.Td(area_rectangulo)])
row4_rec = html.Tr([html.Td("Centroide x (Cx)"), html.Td(cx_rectangulo)])
row5_rec = html.Tr([html.Td("Centroide y (Cy)"), html.Td(cy_rectangulo)])
row6_rec = html.Tr([html.Td("Constante Torsional (J)"), html.Td(j_rectangulo)])
#se crea la tabla con las propiedades establecidas
table_body_rec = [html.Tbody([row1_rec, row2_rec, row3_rec, row4_rec,row5_rec,row6_rec])]
# crea una tabla utilizando el componente dbc.Table de Dash Bootstrap Components.
#se aplican estilos de formato a la tabla, como el color de fondo, la fuente, el color del texto, el peso de la fuente, la alineación del texto y el borde de la tabla.
table_rec = dbc.Table( table_body_rec, bordered=True,
    style={'background-color': 'white', 
                               "font-family": "Arial Narrow", 
                               "color": "purple", 
                               "font-weight": "bold", 
                               "text-align": "center",
                               'border': '0.5px solid purple'}
)

# Se crea una lista de propiedades para circulo: momento de inercia en x y y, area, centroides, y j

row1_cir = html.Tr([html.Td("Inercía (Iy)"), html.Td(iy_circulo)])
row2_cir = html.Tr([html.Td("Inercía (Ix)"), html.Td(ix_circulo)])
row3_cir = html.Tr([html.Td("Área (A)"), html.Td(area_circulo)])
row4_cir = html.Tr([html.Td("Centroide x (Cx)"), html.Td(cx_circulo)])
row5_cir = html.Tr([html.Td("Centroide y (Cy)"), html.Td(cy_circulo)])
row6_cir = html.Tr([html.Td("Constante Torsional (J)"), html.Td(j_circulo)])
#se crea la tabla con las propiedades establecidas
table_body_cir = [html.Tbody([row1_cir, row2_cir, row3_cir, row4_cir,row5_cir,row6_cir])]
# crea una tabla utilizando el componente dbc.Table de Dash Bootstrap Components.
#se aplican estilos de formato a la tabla, como el color de fondo, la fuente, el color del texto, el peso de la fuente, la alineación del texto y el borde de la tabla.
table_cir = dbc.Table( table_body_cir, bordered=True,
    style={'background-color': 'white', 
                               "font-family": "Arial Narrow", 
                               "color": "purple", 
                               "font-weight": "bold", 
                               "text-align": "center",
                               'border': '0.5px solid purple'}
)

# Se crea una lista de propiedades para semicirculo: momento de inercia en x y y, area, centroides, y j

row1_semicir = html.Tr([html.Td("Inercía (Iy)"), html.Td(iy_semicirculo)])
row2_semicir = html.Tr([html.Td("Inercía (Ix)"), html.Td(ix_semicirculo)])
row3_semicir = html.Tr([html.Td("Área (A)"), html.Td(area_semicirculo)])
row4_semicir = html.Tr([html.Td("Centroide x (Cx)"), html.Td(cx_semicirculo)])
row5_semicir = html.Tr([html.Td("Centroide y (Cy)"), html.Td(cy_semicirculo)])
row6_semicir = html.Tr([html.Td("Constante Torsional (J)"), html.Td(j_semicirculo)])
#se crea la tabla con las propiedades establecidas

table_body_semicir = [html.Tbody([row1_semicir, row2_semicir, row3_semicir, row4_semicir,row5_semicir,row6_semicir])]
# crea una tabla utilizando el componente dbc.Table de Dash Bootstrap Components.
#se aplican estilos de formato a la tabla, como el color de fondo, la fuente, el color del texto, el peso de la fuente, la alineación del texto y el borde de la tabla.

table_semicir = dbc.Table( table_body_semicir, bordered=True,
    style={'background-color': 'white', 
                               "font-family": "Arial Narrow", 
                               "color": "purple", 
                               "font-weight": "bold", 
                               "text-align": "center",
                               'border': '0.5px solid purple'}
)

# Se crea una lista de propiedades para cuarto de circulo: momento de inercia en x y y, area, centroides, y j

row1_cuarcir = html.Tr([html.Td("Inercía (Iy)"), html.Td(iy_cuartocirculo)])
row2_cuarcir = html.Tr([html.Td("Inercía (Ix)"), html.Td(ix_cuartocirculo)])
row3_cuarcir = html.Tr([html.Td("Área (A)"), html.Td(area_cuartocirculo)])
row4_cuarcir = html.Tr([html.Td("Centroide x (Cx)"), html.Td(cx_cuartocirculo)])
row5_cuarcir = html.Tr([html.Td("Centroide y (Cy)"), html.Td(cy_cuartocirculo)])
row6_cuarcir = html.Tr([html.Td("Constante Torsional (J)"), html.Td(j_cuartocirculo)])
#se crea la tabla con las propiedades establecidas

table_body_cuartocir = [html.Tbody([row1_cuarcir, row2_cuarcir, row3_cuarcir, row4_cuarcir,row5_cuarcir,row6_cuarcir])]
# crea una tabla utilizando el componente dbc.Table de Dash Bootstrap Components.
#se aplican estilos de formato a la tabla, como el color de fondo, la fuente, el color del texto, el peso de la fuente, la alineación del texto y el borde de la tabla.

table_cuartocir = dbc.Table( table_body_cuartocir, bordered=True,
    style={'background-color': 'white', 
                               "font-family": "Arial Narrow", 
                               "color": "purple", 
                               "font-weight": "bold", 
                               "text-align": "center",
                               'border': '0.5px solid purple'}
)

# Se crea una lista de propiedades para sector de circulo: momento de inercia en x y y, area, centroides, y j

row1_seccir = html.Tr([html.Td("Inercía (Iy)"), html.Td(iy_seccirculo)])
row2_seccir = html.Tr([html.Td("Inercía (Ix)"), html.Td(ix_seccirculo)])
row3_seccir = html.Tr([html.Td("Área (A)"), html.Td(area_seccirculo)])
row4_seccir = html.Tr([html.Td("Centroide x (Cx)"), html.Td(cx_seccirculo)])
row5_seccir = html.Tr([html.Td("Centroide y (Cy)"), html.Td(cy_seccirculo)])
row6_seccir = html.Tr([html.Td("Constante Torsional (J)"), html.Td(j_seccirculo)])
#se crea la tabla con las propiedades establecidas

table_body_seccir = [html.Tbody([row1_seccir, row2_seccir, row3_seccir, row4_seccir,row5_seccir,row6_seccir])]
# crea una tabla utilizando el componente dbc.Table de Dash Bootstrap Components.
#se aplican estilos de formato a la tabla, como el color de fondo, la fuente, el color del texto, el peso de la fuente, la alineación del texto y el borde de la tabla.

table_seccir = dbc.Table( table_body_seccir, bordered=True,
    style={'background-color': 'white', 
                               "font-family": "Arial Narrow", 
                               "color": "purple", 
                               "font-weight": "bold", 
                               "text-align": "center",
                               'border': '0.5px solid purple'}
)

# Se crea una lista de propiedades para triangulo: momento de inercia en x y y, area, centroides, y j

row1_tri = html.Tr([html.Td("Inercía (Iy)"), html.Td(iy_tri)])
row2_tri = html.Tr([html.Td("Inercía (Ix)"), html.Td(ix_tri)])
row3_tri = html.Tr([html.Td("Área (A)"), html.Td(area_tri)])
row4_tri = html.Tr([html.Td("Centroide x (Cx)"), html.Td(cx_tri)])
row5_tri = html.Tr([html.Td("Centroide y (Cy)"), html.Td(cy_tri)])
row6_tri = html.Tr([html.Td("Constante Torsional (J)"), html.Td(j_tri)])
#se crea la tabla con las propiedades establecidas

table_body_tri = [html.Tbody([row1_tri, row2_tri, row3_tri, row4_tri,row5_tri,row6_tri])]
# crea una tabla utilizando el componente dbc.Table de Dash Bootstrap Components.
#se aplican estilos de formato a la tabla, como el color de fondo, la fuente, el color del texto, el peso de la fuente, la alineación del texto y el borde de la tabla.

table_tri = dbc.Table( table_body_tri, bordered=True,
    style={'background-color': 'white', 
                               "font-family": "Arial Narrow", 
                               "color": "purple", 
                               "font-weight": "bold", 
                               "text-align": "center",
                               'border': '0.5px solid purple'}
)

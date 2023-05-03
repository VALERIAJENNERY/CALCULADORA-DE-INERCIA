import dash # Se importa Dash 
from dash import html # Se importa Html 
import dash_bootstrap_components as dbc  #Se importan los componentes de Bootstrap

# importar fronted
from fronted.navegador.navegador import navegador # Se importa la variable navegador
from fronted.arriba.arriba import arriba  # Se importa la variable arriba
from fronted.botones.botones import botones # Se importa la variable botones
from fronted.botones.botones import aceptar # Se importa la variable aceptar
from fronted.datos.datos1 import datos1 # Se importa la variable datos1
from fronted.datos.datos2 import datos2 # Se importa la variable datos2
from fronted.abajo.abajo import abajo # Se importa la variable abajo

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP]) # Se importan los temas de Bootstrap

# Se genera un cuadro que contenga toda la aplicación 
app.layout = dbc.Container(

    [
        dbc.Row(
            [
                dbc.Col(navegador, md=12, style ={'background-color':'white'}), # Se genera una columna para el titulo
                dbc.Col('Valeria Hernandez - 20222579021', md=12, style ={'background-color':'pink'}), # Se genera una columna para los nombres 
                dbc.Col('María Rojas - 20222579030', md=12, style ={'background-color':'pink'}), # Se genera una columna para los nombres
                dbc.Col(arriba, md=12, style ={'background-color':'white'}), # Se genera una columna para el subtitulo
                dbc.Col(botones, md=12, style ={'background-color':'white'}), # Se genera una columna para los botones 
                dbc.Col(datos1, md=8, style ={'background-color':'white'}), # Se genera una columna para el primer dato de acceso 
                dbc.Col(datos2, md=8, style ={'background-color':'white'}),# Se genera una columna para el segundo dato de acceso 
                dbc.Col(aceptar, md=8, style ={'background-color':'white'}), # Se genera una columna parael botón de calcular 
                dbc.Col(abajo, md=12, style ={'background-color':'pink'}), # Se genera una columna que contenga la gráfica y los datos de salida
            ]
        )
    ]
)
# para crear la visualización
if __name__ == "__main__":
    app.run_server(debug = True)
    

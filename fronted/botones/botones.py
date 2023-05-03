import dash_bootstrap_components as dbc # importar los componentes de Bootstrap 
from dash import html # Importar Html de dash 

# Se crea una variable que contenga los botones 
botones = html.Div(
    [
        dbc.Button("Rectangulo", color="danger", className="me-1"), # Se genera un boton con una leyenda en particular, y color rosa 
        dbc.Button("Circulo", color="danger", className="me-1"), # Se genera un boton con una leyenda en particular, y color rosa
        dbc.Button("Semicirculo", color="danger", className="me-1"), # Se genera un boton con una leyenda en particular, y color rosa
        dbc.Button("Cuarto de circulo", color="danger", className="me-1"), # Se genera un boton con una leyenda en particular, y color rosa
        dbc.Button("Arco", color="danger", className="me-1"), # Se genera un boton con una leyenda en particular, y color rosa
        dbc.Button("Triangulo", color="danger", className="me-1"), # Se genera un boton con una leyenda en particular, y color rosa
        html.Hr(),
    ])
    
    # Se genera una variable que contenga el  botón que nos ayudará a calcular
    
aceptar = html.Div(
    [
        dbc.Button("Calcular", outline=True, color="danger", className="me-1"), # Se genera un bton con borde rosa y el fondo blanco
        html.Hr(), # Se genera una división 
    ]
)
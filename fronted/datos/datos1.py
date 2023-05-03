import dash_bootstrap_components as dbc # importar los componentes de Bootstrap

# Se crea una variable que contenga los siguientes datos:
datos1 = dbc.Row(
    [
        dbc.Label("Altura (h)", html_for="h", width=2), #Se crea una casilla que contenga el titulo 
        dbc.Col(
            dbc.Input( # Se crea un imput para que el usuario logre digitar el dato solicitado
                type="Altura (h)", id="h", placeholder="Escriba la altura, ej. 15" # Se le escribe un ejemplo.
            ),
            width=10,# para ponerle tamaño 
        ),
    ],
    className="mb-3",
    
)

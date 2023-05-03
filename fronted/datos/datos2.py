import dash_bootstrap_components as dbc # importar los componentes de Bootstrap

# Se crea una variable que contenga los siguientes datos:
datos2 = dbc.Row(
    [
        dbc.Label("Base (b)", html_for="b", width=2), #Se crea una casilla que contenga el titulo 
        dbc.Col(
            dbc.Input(# Se crea un imput para que el usuario logre digitar el dato solicitado
                type="Base (b)",
                id="b",
                placeholder="Escriba la base, ej. 15", # Se le escribe un ejemplo.
            ),
            width=10, # para ponerle tamaño 
        ),
    ],
    className="mb-3",
)


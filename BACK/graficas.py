import matplotlib.pyplot as plt
import numpy as np
import io
import base64

def graficar_rectangulo(entrada_base_rec,entrada_altura_rec):
    #  Se crea la figura y el objeto de los ejes
    
    fig, ax = plt.subplots()

    # Dibujar el rectángulo en los ejes
    rect = plt.Rectangle((0, 0), entrada_base_rec, entrada_altura_rec, linewidth=1, edgecolor='r', facecolor='grey')
    ax.add_patch(rect)

    # Establecer las etiquetas de los ejes y el título del gráfico
    ax.set_xlabel('Base')
    ax.set_ylabel('Altura')
    ax.set_title('Rectángulo de Base {} y Altura {}'.format(entrada_base_rec,entrada_altura_rec))

    # Establecer los límites de los ejes
    ax.set_xlim(0, entrada_base_rec + 0.1 * entrada_base_rec)
    ax.set_ylim(0, entrada_altura_rec + 0.1 * entrada_altura_rec)

    # Guardar la figura en un objeto BytesIO
    fig_buffer = io.BytesIO()
    plt.savefig(fig_buffer, format='png')
    plt.close()

    fig_buffer.seek(0)

    encoded_image = base64.b64encode(fig_buffer.getvalue()).decode()
    # Crear la figura HTML con Dash
    return encoded_image
    

def graficar_circulo(entrada_circulo):
    # Crear un arreglo de valores x e y
    x = np.linspace(-entrada_circulo, entrada_circulo, 1000)
    y = np.linspace(-entrada_circulo, entrada_circulo, 1000)

    # Crear una matriz con los valores de x e y
    X, Y = np.meshgrid(x, y)

    # Crear una matriz de distancias
    D = np.sqrt(X**2 + Y**2)

    # Crear la figura y el objeto de los ejes
    fig, ax = plt.subplots()

    # Dibujar el círculo en los ejes
    circulo = plt.Circle((0, 0), entrada_circulo, linewidth=1, edgecolor='r', facecolor='grey')
    ax.add_artist(circulo)

    # Establecer las etiquetas de los ejes y el título del gráfico
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Círculo de Radio {}'.format(entrada_circulo))

    # Establecer los límites de los ejes
    ax.set_xlim(-entrada_circulo - 0.1 * entrada_circulo, entrada_circulo + 0.1 * entrada_circulo)
    ax.set_ylim(-entrada_circulo - 0.1 * entrada_circulo, entrada_circulo + 0.1 * entrada_circulo)

    # Guardar la figura en un objeto BytesIO
    fig_buffer = io.BytesIO()
    plt.savefig(fig_buffer, format='png')
    plt.close()

    fig_buffer.seek(0)

    encoded_image = base64.b64encode(fig_buffer.getvalue()).decode()
    # Crear la figura HTML con Dash
    return encoded_image


def graficar_semicirculo(entrada_semicirculo):
    # Crear un arreglo de valores x para el semicírculo
    x = np.linspace(-entrada_semicirculo, entrada_semicirculo, 1000)

    # Crear un arreglo de valores y para la mitad superior
    y = np.sqrt(entrada_semicirculo**2 - x**2)
    y = np.where(y.imag==0, y.real, np.nan)

    # Crear una figura y objeto de ejes
    fig, ax = plt.subplots()

    # Graficar el semicírculo en los ejes
    ax.plot(x, y, linewidth=1, color='r')
    ax.plot(x, -y, linewidth=1, color='r')

    # Establecer las etiquetas de los ejes y el título del gráfico
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Semicírculo de Radio {}'.format(entrada_semicirculo))

    # Establecer los límites de los ejes
    ax.set_xlim(-1.1 * entrada_semicirculo, 1.1 * entrada_semicirculo)
    ax.set_ylim(-0.1 * entrada_semicirculo, 1.1 * entrada_semicirculo)

    # Guardar la figura en un objeto BytesIO
    fig_buffer = io.BytesIO()
    plt.savefig(fig_buffer, format='png')
    plt.close()

    fig_buffer.seek(0)

    encoded_image = base64.b64encode(fig_buffer.getvalue()).decode()
    # Crear la figura HTML con Dash
    return encoded_image


def graficar_cuarto_circulo(entrada_cuartocirculo):
    # Crear un arreglo de valores x para la mitad superior
    x = np.linspace(0, entrada_cuartocirculo, 1000)

    # Crear un arreglo de valores y para la mitad superior
    y = np.sqrt(entrada_cuartocirculo**2 - x**2)

    # Crear una figura y objeto de ejes
    fig, ax = plt.subplots()

    # Graficar el semicírculo en los ejes
    ax.plot(x, y, linewidth=1, color='r')
    ax.plot(x, -y, linewidth=1, color='r')

    # Establecer las etiquetas de los ejes y el título del gráfico
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Cuarto de círculo de Radio {}'.format(entrada_cuartocirculo))

    # Establecer los límites de los ejes
    ax.set_xlim(-0.1 * entrada_cuartocirculo, entrada_cuartocirculo + 0.1 * entrada_cuartocirculo)
    ax.set_ylim(0, entrada_cuartocirculo + 0.1 * entrada_cuartocirculo)
    # Guardar la figura en un objeto BytesIO
    fig_buffer = io.BytesIO()
    plt.savefig(fig_buffer, format='png')
    plt.close()

    fig_buffer.seek(0)

    encoded_image = base64.b64encode(fig_buffer.getvalue()).decode()
    # Crear la figura HTML con Dash
    return encoded_image



def graficar_sector(entrada_radio_sector,entrada_angulo_sector):
    # Verificar que el radio esté en el rango correcto
    if entrada_radio_sector <= 0:
        raise ValueError("El radio 'r' debe ser mayor que cero.")
    
    # Asegurarse de que el ángulo está en el rango correcto
    entrada_angulo_sector = entrada_angulo_sector % 360
    
    # Crear la lista de valores para el sector
    valores = [entrada_angulo_sector, 360 - entrada_angulo_sector]
    
    # Crear la lista de etiquetas
    etiquetas = ['Área del sector', '']
    
    # Crear una lista de colores para el sector y el área no sombreada
    colores = ['r', 'grey']
    
    # Crear una figura y objeto de ejes
    fig, ax = plt.subplots()

    # Graficar el sector en los ejes
    ax.pie(valores, labels=etiquetas, colors=colores, radius=entrada_radio_sector, startangle=90-entrada_angulo_sector/2, counterclock=False)

    # Establecer el título del gráfico
    ax.set_title('Sector Circular de Radio {} y Ángulo {}'.format(entrada_radio_sector, entrada_angulo_sector))

    # Establecer el aspecto de los ejes para que parezcan un círculo
    ax.axis('equal')
    # Guardar la figura en un objeto BytesIO
    fig_buffer = io.BytesIO()
    plt.savefig(fig_buffer, format='png')
    plt.close()

    fig_buffer.seek(0)

    encoded_image = base64.b64encode(fig_buffer.getvalue()).decode()
    # Crear la figura HTML con Dash
    return encoded_image


def graficar_triangulo(b, h, a):
    # Verificar que la base, altura y a estén en el rango correcto
    if b <= 0 or h <= 0 or a < 0 or a > b:
        raise ValueError("La base y la altura deben ser mayores que cero y a debe estar en el rango [0, b].")
    
    # Calcular la coordenada x del vértice superior del triángulo
    x_top = a
    # Calcular las coordenadas de los vértices del triángulo
    x = [0, b, x_top]
    y = [0, 0, h]

    # Crear una figura y objeto de ejes
    fig, ax = plt.subplots()

    # Graficar el triángulo en los ejes
    ax.fill(x, y, color='grey')

    # Agregar línea horizontal para la distancia a
    ax.hlines(h, 0, a, color='r', linestyle='--')

    # Agregar etiqueta para la distancia a
    ax.text(a/2, h+0.05*h, 'a = {}'.format(a), fontsize=12, ha='center', va='bottom')

    # Establecer el título del gráfico
    ax.set_title('Triángulo de Base {}, Altura {} y a = {}'.format(b, h, a))

    # Establecer los límites de los ejes
    ax.set_xlim(left=-0.1*b, right=1.1*b)
    ax.set_ylim(bottom=-0.1*h, top=1.1*h)

    # Etiquetar los ejes
    ax.set_xlabel('Base')
    ax.set_ylabel('Altura')

    # Mostrar el gráfico
    plt.show()

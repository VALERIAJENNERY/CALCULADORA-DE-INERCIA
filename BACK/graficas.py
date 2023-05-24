import matplotlib.pyplot as plt  # Importa el módulo pyplot de matplotlib y lo asigna a la variable 'plt'
import numpy as np  # Importa el módulo numpy y lo asigna a la variable 'np'
import io  # Importa el módulo io
import base64  # Importa el módulo base64


def graficar_rectangulo(entrada_base_rec,entrada_altura_rec):
    #  Se crea la figura y el objeto de los ejes
    
    fig, ax = plt.subplots()

    # Dibujar el rectángulo en los ejes
    rect = plt.Rectangle((0, 0), entrada_base_rec, entrada_altura_rec, linewidth=1, edgecolor='#40E0D0', facecolor='#FFD1DC')
    ax.add_patch(rect)

    # Para dibujar el centroide de la figura:
    plt.scatter(entrada_base_rec/2, entrada_altura_rec/2, color = "black",marker="o")
    plt.text(entrada_base_rec/2+0.1, entrada_altura_rec/2+0.1, 'C ({:.1f}, {:.1f})'.format(entrada_base_rec/2, entrada_altura_rec/2), fontsize=12, style="italic") 
    
    # Establecer las etiquetas de los ejes y el título del gráfico
    ax.set_xlabel('Eje x',fontsize=10, style="italic", fontweight="bold")
    ax.set_ylabel('Eje y',fontsize=10, style="italic", fontweight="bold")
    ax.set_title('Rectángulo de Base {} m y Altura {} m'.format(entrada_base_rec,entrada_altura_rec),fontsize=15, style="italic", fontweight="bold")

    # Agregar la cota horizontal 
    plt.annotate('',
                 xy=(0, entrada_altura_rec+0.3),  # Punto de partida de la línea
                 xytext=(entrada_base_rec, entrada_altura_rec+0.3),  # Punto de llegada de la línea
                 arrowprops=dict(arrowstyle='<->'))  # Estilo de flecha bidireccional
    
    # Agregar texto de la cota horizontal 
    texto = '{} m'.format(entrada_base_rec)
    x_texto = entrada_base_rec / 2
    y_texto = entrada_altura_rec + 0.35
    plt.text(x_texto, y_texto, texto, ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Agregar la cota vertical
    plt.annotate('',
                xy=(entrada_base_rec+0.3, 0),  # Punto de partida de la línea
                xytext=(entrada_base_rec+0.3, entrada_altura_rec),  # Punto de llegada de la línea
                arrowprops=dict(arrowstyle='<->'))  # Estilo de flecha bidireccional

    # Agregar texto de la cota vertical
    texto1 = '{} m'.format(entrada_altura_rec)
    x_texto1 = entrada_base_rec + 0.4
    y_texto1 = entrada_altura_rec / 2
    plt.text(x_texto1, y_texto1, texto1, ha='left', va='center', fontsize=10, fontweight='bold')

    # Establecer los límites de los ejes
    ax.set_xlim(0, entrada_base_rec + 0.2 * entrada_base_rec)
    ax.set_ylim(0, entrada_altura_rec + 0.2 * entrada_altura_rec)
    plt.grid(color='gray', ls="--", lw = 0.3) # Para poner la grilla.

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
    circulo = plt.Circle((0, 0), entrada_circulo, linewidth=1, edgecolor='#40E0D0', facecolor='#FFD1DC')
    ax.add_artist(circulo)
    
    # Para dibujar el centroide de la figura:
    plt.scatter(0, 0, color = "black",marker="o")
    plt.text(0+0.1, 0+0.1, 'C ({}, {})'.format(0,0), fontsize=12, style="italic") 
    

    # Establecer las etiquetas de los ejes y el título del gráfico
    ax.set_xlabel('Eje x',fontsize=10, style="italic", fontweight="bold")
    ax.set_ylabel('Eje y',fontsize=10, style="italic", fontweight="bold")
    ax.set_title('Círculo de Radio {} m'.format(entrada_circulo),fontsize=15, style="italic", fontweight="bold")

    # Establecer los límites de los ejes
    ax.set_xlim(-entrada_circulo - 0.1 * entrada_circulo, entrada_circulo + 0.1 * entrada_circulo)
    ax.set_ylim(-entrada_circulo - 0.1 * entrada_circulo, entrada_circulo + 0.1 * entrada_circulo)
    # Agregar líneas de grilla con grosor diferente en x=0 e y=0
    ax.axhline(0, color='black', ls="-", lw=0.5)  # Línea horizontal en y=0
    ax.axvline(0, color='black', ls="-", lw=0.5)  # Línea vertical en x=0
    
    plt.grid(color='gray', ls="--", lw = 0.3) # Para poner la grilla.
    
    # Agregar la cota del radio
    plt.annotate('',
                 xy=(0, 0),  # Punto de partida de la línea
                 xytext=(-np.cos(np.deg2rad(45)) * entrada_circulo, -np.sin(np.deg2rad(45)) * entrada_circulo),  # Punto de llegada de la línea
                 arrowprops=dict(arrowstyle='<->'))  # Estilo de flecha bidireccional

    # Agregar texto del radio 
    texto1 = '{} m'.format(entrada_circulo)
    x_texto1 = -(np.cos(np.deg2rad(45)) * entrada_circulo / 2) + 0.3
    y_texto1 = -(np.sin(np.deg2rad(45)) * entrada_circulo / 2) - 0.2
    plt.text(x_texto1, y_texto1, texto1, ha='left', va='center', fontsize=10, fontweight='bold')

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
    ax.plot(x, y, linewidth=1, color='#40E0D0')
    ax.plot(x, -y, linewidth=1, color='#40E0D0')
    
    # Sombrear la parte dentro del semicírculo
    ax.fill_between(x, y, -y, color='#FFD1DC', alpha=0.3)

    # Establecer las etiquetas de los ejes y el título del gráfico
    ax.set_xlabel('Eje x',fontsize=10, style="italic", fontweight="bold")
    ax.set_ylabel('Eje y',fontsize=10, style="italic", fontweight="bold")
    ax.set_title('Semicírculo de Radio {} m'.format(entrada_semicirculo),fontsize=15, style="italic", fontweight="bold")

    # Establecer los límites de los ejes
    ax.set_xlim(-1.1 * entrada_semicirculo, 1.1 * entrada_semicirculo)
    ax.set_ylim(0, 1.1 * entrada_semicirculo)
    
    # Para dibujar el centroide de la figura:
    
    C=((4/(3* np.pi)) * entrada_semicirculo)
    plt.scatter(0, C, marker="o", color="black")
    plt.text(0 + 0.1, C + 0.1, 'C({}, {:.1f})'.format(0, C), fontsize=12, style="italic")

    # Agregar la cota del radio
    plt.annotate('',
                 xy=(0, 0),  # Punto de partida de la línea
                 xytext=(np.cos(np.deg2rad(45+90)) * entrada_semicirculo, np.sin(np.deg2rad(45+90)) * entrada_semicirculo),  # Punto de llegada de la línea
                 arrowprops=dict(arrowstyle='<->'))  # Estilo de flecha bidireccional

    # Agregar texto del radio 
    texto1 = '{} m'.format(entrada_semicirculo)
    x_texto1 = (np.cos(np.deg2rad(45+90)) * entrada_semicirculo / 2) + 0.1
    y_texto1 = (np.sin(np.deg2rad(45+90)) * entrada_semicirculo / 2) + 0.2
    plt.text(x_texto1, y_texto1, texto1, ha='left', va='center', fontsize=10, fontweight='bold')
    
    plt.grid(color='gray', ls="--", lw = 0.3) # Para poner la grilla.

    # Guardar la figura en un objeto BytesIO
    fig_buffer = io.BytesIO()
    plt.savefig(fig_buffer, format='png')
    plt.close()

    fig_buffer.seek(0)

    encoded_image = base64.b64encode(fig_buffer.getvalue()).decode()
    # Crear la figura HTML con Dash
    return encoded_image


def graficar_cuarto_circulo(entrada_cuartocirculo):
    # Crear un arreglo de valores x para el cuarto de círculo
    x = np.linspace(0, entrada_cuartocirculo, 1000)

    # Crear un arreglo de valores y para el cuarto de círculo superior
    y = np.sqrt(entrada_cuartocirculo**2 - x**2)

    # Crear una figura y objeto de ejes
    fig, ax = plt.subplots()

    # Graficar el cuarto de círculo en los ejes
    ax.plot(x, y, linewidth=1, color='#40E0D0')
    ax.plot(x, -y, linewidth=1, color='#40E0D0')

    # Sombrear el cuarto de círculo superior
    ax.fill_between(x, y, where=(x >= 0), color='#FFD1DC', alpha=0.3)

    # Establecer las etiquetas de los ejes y el título del gráfico
    ax.set_xlabel('Eje x', fontsize=10, style="italic", fontweight="bold")
    ax.set_ylabel('Eje y', fontsize=10, style="italic", fontweight="bold")
    ax.set_title('Cuarto de Círculo de Radio {} m'.format(entrada_cuartocirculo), fontsize=15, style="italic", fontweight="bold")

    # Establecer los límites de los ejes
    ax.set_xlim(0, entrada_cuartocirculo + 0.1 * entrada_cuartocirculo)
    ax.set_ylim(0, entrada_cuartocirculo + 0.1 * entrada_cuartocirculo)

    # Para dibujar el centroide de la figura:
    
    C=((4/(3* np.pi)) * entrada_cuartocirculo)
    plt.scatter(C, C, marker="o", color="black")
    plt.text(C + 0.1, C + 0.1, 'C({:.1f}, {:.1f})'.format(C, C), fontsize=12, style="italic")

    plt.grid(color='gray', ls="--", lw=0.3) # Para poner la grilla.
    
    # Agregar la cota horizontal 
    plt.annotate('',
                 xy=(0, entrada_cuartocirculo+0.1),  # Punto de partida de la línea
                 xytext=(entrada_cuartocirculo, entrada_cuartocirculo+0.1),  # Punto de llegada de la línea
                 arrowprops=dict(arrowstyle='<->'))  # Estilo de flecha bidireccional
    
    # Agregar texto de la cota horizontal 
    texto = '{} m'.format(entrada_cuartocirculo)
    x_texto = entrada_cuartocirculo / 2
    y_texto = entrada_cuartocirculo + 0.1
    plt.text(x_texto, y_texto, texto, ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Agregar la cota vertical
    plt.annotate('',
                xy=(entrada_cuartocirculo+0.08, 0),  # Punto de partida de la línea
                xytext=(entrada_cuartocirculo+0.08, entrada_cuartocirculo),  # Punto de llegada de la línea
                arrowprops=dict(arrowstyle='<->'))  # Estilo de flecha bidireccional

    # Agregar texto de la cota vertical
    texto1 = '{} m'.format(entrada_cuartocirculo)
    x_texto1 = entrada_cuartocirculo + 0.1
    y_texto1 = entrada_cuartocirculo / 2
    plt.text(x_texto1, y_texto1, texto1, ha='left', va='center', fontsize=10, fontweight='bold')   
    
    # Guardar la figura en un objeto BytesIO
    fig_buffer = io.BytesIO()
    plt.savefig(fig_buffer, format='png')
    plt.close()

    fig_buffer.seek(0)

    encoded_image = base64.b64encode(fig_buffer.getvalue()).decode()
    # Crear la figura HTML con Dash
    return encoded_image



def graficar_sector (entrada_radio_sector, entrada_angulo_sector):
    # Verificar que el radio esté en el rango correcto
    if entrada_radio_sector <= 0:
        raise ValueError("El radio 'r' debe ser mayor que cero.")
    
    # Asegurarse de que el ángulo está en el rango correcto
    entrada_angulo_sector = entrada_angulo_sector % 360
    
    # Crear la lista de valores para el sector
    valores = [entrada_angulo_sector, 360 - entrada_angulo_sector]

    
    # Crear una lista de colores para el sector y el área no sombreada
    colores = ['#FFD1DC', 'white']
    
    # Crear una figura y objeto de ejes
    fig, ax = plt.subplots()

    # Graficar el sector en los ejes
    ax.pie(valores, colors=colores, radius=entrada_radio_sector, startangle=360+entrada_angulo_sector/2, counterclock=False, wedgeprops={'linewidth': 1, 'edgecolor': '#40E0D0'})

 
    # Establecer el título del gráfico
    ax.set_title('Sector Circular de Radio {} m y Ángulo {}°'.format(entrada_radio_sector, entrada_angulo_sector),fontsize=15, style="italic", fontweight="bold")
    
    # Establecer las etiquetas de los ejes
    ax.set_xlabel('Eje X',fontsize=10, style="italic", fontweight="bold")
    ax.set_ylabel('Eje Y',fontsize=10, style="italic", fontweight="bold")

    # Establecer el aspecto de los ejes para que parezcan un círculo
    ax.axis('equal')
    
    # Agregar ejes con flechas
    ax.annotate('', xy=(entrada_radio_sector + 1, 0), xytext=(-entrada_radio_sector - 1, 0), arrowprops=dict(arrowstyle='<->', lw=0.5))
    ax.annotate('', xy=(0, entrada_radio_sector + 0.4), xytext=(0, -entrada_radio_sector - 0.4), arrowprops=dict(arrowstyle='<->', lw=0.5))
    
    # Hago un señalización con flecha
    px = np.cos(np.deg2rad(entrada_angulo_sector/2)) * entrada_radio_sector/2
    py = np.sin(np.deg2rad(entrada_angulo_sector/2)) * entrada_radio_sector/2
    # Hago un señalización con flecha
    nota = plt.annotate(r'{}°'.format(entrada_angulo_sector),
         xy=(px, py),
         xycoords='data',
         xytext=(px, -py),
         fontsize=9,
         arrowprops=dict(arrowstyle="->",
         connectionstyle="arc3,rad=.2"))
    
    # Agregar la cota del radio
    plt.annotate('',
                 xy=(0, 0),  # Punto de partida de la línea
                 xytext=(-np.cos(np.deg2rad(45)) * entrada_radio_sector, np.sin(np.deg2rad(45)) * entrada_radio_sector),  # Punto de llegada de la línea
                 arrowprops=dict(arrowstyle='<->'))  # Estilo de flecha bidireccional

    # Agregar texto del radio 
    texto1 = '{} m'.format(entrada_radio_sector)
    x_texto1 = (-np.cos(np.deg2rad(45)) * entrada_radio_sector / 2) - 1
    y_texto1 = (np.sin(np.deg2rad(45)) * entrada_radio_sector / 2)
    plt.text(x_texto1, y_texto1, texto1, ha='left', va='center', fontsize=10, fontweight='bold')
    
    # Agregar el centroide 
    C=2*entrada_radio_sector*(np.sin(np.deg2rad(entrada_angulo_sector/2)))/((3/2)*np.deg2rad(entrada_angulo_sector))
    plt.scatter(C, 0, marker="o", color="black")
    plt.text(C,  0.3, 'C({:.1f}, {})'.format(C, 0), fontsize=9, style="italic")
    
    # Guardar la figura en un objeto BytesIO
    fig_buffer = io.BytesIO()
    plt.savefig(fig_buffer, format='png')
    plt.close()

    fig_buffer.seek(0)

    encoded_image = base64.b64encode(fig_buffer.getvalue()).decode()
    # Crear la figura HTML con Dash
    return encoded_image


def graficar_triangulo(entrada_base_trian,entrada_altura_trian,entrada_a_trian):
    # Verificar que la base, altura y a estén en el rango correcto
    if entrada_base_trian <= 0 or entrada_altura_trian <= 0 or entrada_a_trian < 0 or entrada_a_trian > entrada_base_trian:
        raise ValueError("La base y la altura deben ser mayores que cero y a debe estar en el rango [0, b].")
    
    # Calcular la coordenada x del vértice superior del triángulo
    x_top = entrada_a_trian
    # Calcular las coordenadas de los vértices del triángulo
    x = [0, entrada_base_trian, x_top]
    y = [0, 0, entrada_altura_trian]

    # Crear una figura y objeto de ejes
    fig, ax = plt.subplots()
    
    # Agregar el borde del triángulo
    ax.plot(x + [0], y + [0], color='#40E0D0', linewidth=1)
    
    # Graficar el triángulo en los ejes
    ax.fill(x, y, color='#FFD1DC')


    # Establecer el título del gráfico
    ax.set_title('Triángulo de Base {} m, Altura {} m  y A = {} m '.format(entrada_base_trian, entrada_altura_trian, entrada_a_trian),fontsize=15, style="italic", fontweight="bold")

    # Establecer los límites de los ejes
    ax.set_xlim(left=0, right=1.2*entrada_base_trian)
    ax.set_ylim(bottom=0, top=1.2*entrada_altura_trian)

    # Etiquetar los ejes
    ax.set_xlabel('Eje x',fontsize=10, style="italic", fontweight="bold")
    ax.set_ylabel('Eje y',fontsize=10, style="italic", fontweight="bold")
    plt.grid(color='gray', ls="--", lw=0.3) # Para poner la grilla.
    
    # Agregar la cota horizontal total
    plt.annotate('',
                 xy=(0, entrada_altura_trian+0.7),  # Punto de partida de la línea
                 xytext=(entrada_base_trian, entrada_altura_trian+0.7),  # Punto de llegada de la línea
                 arrowprops=dict(arrowstyle='<->'))  # Estilo de flecha bidireccional
    
    # Agregar texto de la cota horizontal total
    texto = '{} m'.format(entrada_base_trian)
    x_texto = entrada_base_trian / 2
    y_texto = entrada_altura_trian + 0.7
    plt.text(x_texto, y_texto, texto, ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Agregar la cota horizontal A
    plt.annotate('',
                 xy=(0, entrada_altura_trian+0.3),  # Punto de partida de la línea
                 xytext=(entrada_a_trian, entrada_altura_trian+0.3),  # Punto de llegada de la línea
                 arrowprops=dict(arrowstyle='<->'))  # Estilo de flecha bidireccional
    
    # Agregar texto de la cota horizontal A
    texto = '{} m'.format(entrada_a_trian)
    x_texto = entrada_a_trian / 2
    y_texto = entrada_altura_trian + 0.3
    plt.text(x_texto, y_texto, texto, ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Agregar la cota vertical
    plt.annotate('',
                xy=(entrada_base_trian+0.3, 0),  # Punto de partida de la línea
                xytext=(entrada_base_trian+0.3, entrada_altura_trian),  # Punto de llegada de la línea
                arrowprops=dict(arrowstyle='<->'))  # Estilo de flecha bidireccional

    # Agregar texto de la cota vertical
    texto1 = '{} m'.format(entrada_altura_trian)
    x_texto1 = entrada_base_trian + 0.4
    y_texto1 = entrada_altura_trian / 2
    plt.text(x_texto1, y_texto1, texto1, ha='left', va='center', fontsize=10, fontweight='bold')
    
    # Agregar el centroide 
    Cx=(entrada_a_trian+entrada_base_trian)/3
    Cy=entrada_altura_trian/3
    plt.scatter(Cx, Cy, marker="o", color="black")
    plt.text(Cx,  Cy+0.2, 'C ({:.1f}, {:.1f})'.format(Cx, Cy), fontsize=10, style="italic")
    

    # Guardar la figura en un objeto BytesIO
    fig_buffer = io.BytesIO()
    plt.savefig(fig_buffer, format='png')
    plt.close()

    fig_buffer.seek(0)

    encoded_image = base64.b64encode(fig_buffer.getvalue()).decode()
    # Crear la figura HTML con Dash
    return encoded_image

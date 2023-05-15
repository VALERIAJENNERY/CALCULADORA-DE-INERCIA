
import math #Se importo la libreria math para poder utilizar pi

def a_rectangulo(entrada_base_rec,entrada_altura_rec): #Se crea una funcion para calcular el area de la figura
    area_rec=entrada_base_rec*entrada_altura_rec #Se calcula el área 
    return area_rec

def a_circulo(entrada_circulo): #Se crea una funcion para calcular el area de la figura
    area_cir=math.pi*(entrada_circulo**2) #Se calcula el área
    print("El área del círculo es: ", area_cir, "m\xb2") #Se imprime el resultado

def a_semicirculo(entrada_semicirculo): #Se crea una funcion para calcular el area de la figura
    area_semicir=(math.pi*(entrada_semicirculo**2))/2 #Se calcula el área
    print("El área del semicírculo es: ", area_semicir, "m\xb2") #Se imprime el resultado


def a_cuartodecirculo (entrada_cuartocirculo): #Se crea una funcion para calcular el area de la figura
    area_cuarcir=(math.pi*(entrada_cuartocirculo**2))/4 #Se calcula el área
    print("El área del cuarto de círculo es: ", area_cuarcir, "m\xb2") #Se imprime el resultado


def a_sectorcircular (entrada_radio_sector,entrada_angulo_sector): #Se crea una funcion para calcular el area de la figura
    area_seccir=(math.pi*(entrada_radio_sector**2))*(entrada_angulo_sector/2)/360 #Se calcula el área
    print("El área del sector circular es: ", area_seccir, "m\xb2") #Se imprime el resultado


def a_triangulo (entrada_base_trian,entrada_altura_trian): #Se crea una funcion para calcular el area de la figura
    area_tri=entrada_base_trian*entrada_altura_trian #Se calcula el área
    print("El área del triángulo es: ", area_tri, "m\xb2") #Se imprime el resultado

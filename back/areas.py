
import math #Se importo la libreria math para poder utilizar pi

def a_rectangulo(b,h): #Se crea una funcion para calcular el area de la figura
    area_rec=b*h #Se calcula el área 
    print("El área del rectángulo es: ", area_rec, "m\xb2") #Se imprime el resultado

a_rectangulo(5,2) #Se llama a la función

def a_circulo(r): #Se crea una funcion para calcular el area de la figura
    area_cir=math.pi*(r**2) #Se calcula el área
    print("El área del círculo es: ", area_cir, "m\xb2") #Se imprime el resultado


a_circulo(2) #Se llama a la función


def a_semicirculo(r): #Se crea una funcion para calcular el area de la figura
    area_semicir=(math.pi*(r**2))/2 #Se calcula el área
    print("El área del semicírculo es: ", area_semicir, "m\xb2") #Se imprime el resultado
a_semicirculo(2) #Se llama a la función

def a_cuartodecirculo (r): #Se crea una funcion para calcular el area de la figura
    area_cuarcir=(math.pi*(r**2))/4 #Se calcula el área
    print("El área del cuarto de círculo es: ", area_cuarcir, "m\xb2") #Se imprime el resultado
a_cuartodecirculo (2) #Se llama a la función

def a_sectorcircular (r,an): #Se crea una funcion para calcular el area de la figura
    area_seccir=(math.pi*(r**2))*(an/2)/360 #Se calcula el área
    print("El área del sector circular es: ", area_seccir, "m\xb2") #Se imprime el resultado
a_sectorcircular (2,30) #Se llama a la función

def a_triangulo (b,h): #Se crea una funcion para calcular el area de la figura
    area_tri=b*h#Se calcula el área
    print("El área del triángulo es: ", area_tri, "m\xb2") #Se imprime el resultado
a_triangulo (2,30) #Se llama a la función
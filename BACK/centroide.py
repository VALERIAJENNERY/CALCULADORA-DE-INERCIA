import math #Se importo la libreria math para utilizar funciones matematicas

def c_rectangulo(b,h): #Se crea una funcion para calcular el centroide de la figura
    cx_rec=b/2 #Se calculan los centroides para el eje x y y
    cy_rec=h/2
    print("El centroide con respecto al eje x es: ", cx_rec, "m") #Se imprimen los resultados
    print("El centroide con respecto al eje y es: ", cy_rec, "m")

c_rectangulo(5,2) #Se llama a la función

def c_circulo(r):#Se crea una funcion para calcular el centroide de la figura
    cx_cir=r #Se calculan los centroides para el eje x y y
    cy_cir=r
    print("El centroide con respecto al eje x es: ", cx_cir, "m") #Se imprimen los resultados
    print("El centroide con respecto al eje y es: ", cy_cir, "m")

c_circulo(2)#Se llama a la función

def c_semicirculo(r): #Se crea una funcion para calcular el centroide de la figura
    cx_semicir=0 #Se calculan los centroides para el eje x y y
    cy_semicir=4*r/(3*math.pi)
    print("El centroide con respecto al eje x es: ", cx_semicir, "m") #Se imprimen los resultados
    print("El centroide con respecto al eje y es: ", cy_semicir, "m")
c_semicirculo(2) #Se llama a la función

def c_cuartodecirculo (r): #Se crea una funcion para calcular el centroide de la figura
    cx_cuarcir=4*r/(3*math.pi) #Se calculan los centroides para el eje x y y
    cy_cuarcir=4*r/(3*math.pi)
    print("El centroide con respecto al eje x es: ", cx_cuarcir, "m") #Se imprimen los resultados
    print("El centroide con respecto al eje y es: ", cy_cuarcir, "m")
c_cuartodecirculo (2) #Se llama a la función

def c_sectorcircular (r,an): #Se crea una funcion para calcular el centroide de la figura
    cx_seccir=(2*r*(math.sin(an)))/(3*an) #Se calculan los centroides para el eje x y y
    cy_seccir=0
    print("El centroide con respecto al eje x es: ", cx_seccir, "m") #Se imprimen los resultados
    print("El centroide con respecto al eje y es: ", cy_seccir, "m")
c_sectorcircular (2,30) #Se llama a la función

def c_triangulo (b,h,a): #Se crea una funcion para calcular el centroide de la figura
    cx_tri=(a+b)/2 #Se calculan los centroides para el eje x y y
    cy_tri=h/3
    print("El centroide con respecto al eje x es: ", cx_tri, "m") #Se imprimen los resultados
    print("El centroide con respecto al eje y es: ", cy_tri, "m")
c_triangulo (2,30,7) #Se llama a la función
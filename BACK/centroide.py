import math #Se importo la libreria math para utilizar funciones matematicas

def cx_rectangulo(entrada_base_rec,entrada_altura_rec): #Se crea una funcion para calcular el centroide de la figura
    cx_rec=entrada_base_rec/2 #Se calculan los centroides para el eje x 
    
    return cx_rec

def cy_rectangulo(entrada_base_rec,entrada_altura_rec): #Se crea una funcion para calcular el centroide de la figura
     #Se calculan los centroides para el eje  y
    cy_rec=entrada_altura_rec/2
    return cy_rec

def cx_circulo(entrada_circulo):#Se crea una funcion para calcular el centroide de la figura
    cx_cir=entrada_circulo #Se calculan los centroides para el eje x y y
    return cx_cir

def cy_circulo(entrada_circulo):#Se crea una funcion para calcular el centroide de la figura
    cy_cir=entrada_circulo
    return cy_cir
    
def c_semicirculo(r): #Se crea una funcion para calcular el centroide de la figura
    cx_semicir=0 #Se calculan los centroides para el eje x y y

    cy_semicir=4*r/(3*math.pi)
   

def c_cuartodecirculo (r): #Se crea una funcion para calcular el centroide de la figura
    cx_cuarcir=4*r/(3*math.pi) #Se calculan los centroides para el eje x y y
    cy_cuarcir=4*r/(3*math.pi)
   
def c_sectorcircular (r,an): #Se crea una funcion para calcular el centroide de la figura
    cx_seccir=(2*r*(math.sin(an/2)))/((3/2)*an) #Se calculan los centroides para el eje x y y
    cy_seccir=0
    
def c_triangulo (b,h,a): #Se crea una funcion para calcular el centroide de la figura
    cx_tri=(a+b)/2 #Se calculan los centroides para el eje x y y
    cy_tri=h/3
   
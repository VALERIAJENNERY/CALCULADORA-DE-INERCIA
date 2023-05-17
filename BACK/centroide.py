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
    
def cx_semicirculo(entrada_semicirculo): #Se crea una funcion para calcular el centroide de la figura
    cx_semicir=0 #Se calculan los centroides para el eje x y y
    return cx_semicir

def cy_semicirculo(entrada_semicirculo): #Se crea una funcion para calcular el centroide de la figura
    cy_semicir=4*entrada_semicirculo/(3*math.pi)
    return cy_semicir

def cx_cuartodecirculo (entrada_cuartocirculo): #Se crea una funcion para calcular el centroide de la figura
    cx_cuarcir=4*entrada_cuartocirculo/(3*math.pi) #Se calculan los centroides para el eje x y y
    return cx_cuarcir

def cy_cuartodecirculo (entrada_cuartocirculo):
    cy_cuarcir=4*entrada_cuartocirculo/(3*math.pi)
    return cy_cuarcir
   
def cx_sectorcircular (entrada_radio_sector,entrada_angulo_sector): #Se crea una funcion para calcular el centroide de la figura
    cx_seccir=(2*entrada_radio_sector*(math.sin(entrada_angulo_sector/2)))/((3/2)*entrada_angulo_sector) #Se calculan los centroides para el eje x y y
    return cx_seccir

def cy_sectorcircular (entrada_radio_sector,entrada_angulo_sector): 
    cy_seccir=0
    return cy_seccir

def cx_triangulo (entrada_base_trian,entrada_altura_trian,entrada_a_trian): #Se crea una funcion para calcular el centroide de la figura
    cx_tri=(entrada_a_trian+entrada_base_trian)/2 #Se calculan los centroides para el eje x y y
    return cx_tri

def cy_triangulo (entrada_base_trian,entrada_altura_trian,entrada_a_trian):
    cy_tri=entrada_altura_trian/3
    return cy_tri
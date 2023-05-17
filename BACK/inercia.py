import math #Se importo la libreria math para utilizar funciones matematicas

def ix_rectangulo(entrada_base_rec,entrada_altura_rec): #Se crea una funcion para calcular la inercia y la constante torcional  de la figura
    ix_rec=(entrada_base_rec*(entrada_altura_rec**3))/12 #Se realizan los calculos para las inercias y la constante torcional (J)
    return ix_rec

def iy_rectangulo(entrada_base_rec,entrada_altura_rec):   
    iy_rec=(entrada_altura_rec*(entrada_base_rec**3))/12
    return iy_rec

def j_rectangulo(entrada_base_rec,entrada_altura_rec):     
    j_rec=((entrada_base_rec*(entrada_altura_rec**3))/12)+((entrada_altura_rec*(entrada_base_rec**3))/12)
    return j_rec
    
def ix_circulo(entrada_circulo): #Se crea una funcion para calcular la inercia y la constante torcional de la figura
    ix_cir=((math.pi)*(entrada_circulo**4))/4 #Se realizan los calculos para las inercias y la constante torcional (J)
    return ix_cir

def iy_circulo(entrada_circulo): 
    iy_cir=((math.pi)*(entrada_circulo**4))/4
    return iy_cir

def j_circulo(entrada_circulo): 
    j_cir=(((math.pi)*(entrada_circulo**4))/4)+(((math.pi)*(entrada_circulo**4))/4)
    return j_cir


def ix_semicirculo(entrada_semicirculo): #Se crea una funcion para calcular la inercia y la constante torcional de la figura
    ix_semicir=((math.pi)*(entrada_semicirculo**4))/8 #Se realizan los calculos para las inercias y la constante torcional (J)
    return ix_semicir

def iy_semicirculo(entrada_semicirculo): #Se crea una funcion para calcular la inercia y la constante torcional de la figura
    iy_semicir=((math.pi)*(entrada_semicirculo**4))/8
    return iy_semicir

def j_semicirculo(entrada_semicirculo):
    j_semicir=(((math.pi)*(entrada_semicirculo**4))/8)*2
    return j_semicir
    


def ix_cuartodecirculo (entrada_cuartocirculo): #Se crea una funcion para calcular la inercia y la constante torcional de la figura
    ix_cuarcir=0.05488*(entrada_cuartocirculo**4) #Se realizan los calculos para las inercias y la constante torcional (J)
    return ix_cuarcir

def iy_cuartodecirculo (entrada_cuartocirculo):
    iy_cuarcir=0.05488*(entrada_cuartocirculo**4)
    return iy_cuarcir

def j_cuartodecirculo (entrada_cuartocirculo):
    j_cuarcir=0.05488*(entrada_cuartocirculo**4)*2
    return j_cuarcir


def i_sectorcircular (r,an): #Se crea una funcion para calcular la inercia y la constante torcional de la figura
    ix_seccir=(r**4)*((an)-(math.sin(an)))/8 #Se realizan los calculos para las inercias y la constante torcional (J)
    iy_seccir=(r**4)*((an)+(math.sin(an)))/8
    j_seccir=(ix_seccir+iy_seccir)
    print("El momento de inercia con respecto al eje x es: ", ix_seccir, "m\xb3") #Se imprimen los resultados
    print("El momento de inercia con respecto al eje y es: ", iy_seccir, "m\xb3")
    print("La constante torcional y es: ", j_seccir, "m\xb3")


def i_triangulo (b,h,a): #Se crea una funcion para calcular la inercia y la constante torcional de la figura
    ix_tri=b*(h**3)/36 #Se realizan los calculos para las inercias y la constante torcional (J)
    iy_tri=b*(h**3)*((a**2)-a*b+(b**2))/36
    j_tri=(ix_tri+iy_tri)
    print("El momento de inercia con respecto al eje x es: ", ix_tri, "m\xb3") #Se imprimen los resultados
    print("El momento de inercia con respecto al eje y es: ", iy_tri, "m\xb3")
    print("La constante torcional y es: ", j_tri, "m\xb3")

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
    ix_semicir=0.1098*(entrada_semicirculo**4) #Se realizan los calculos para las inercias y la constante torcional (J)
    return ix_semicir

def iy_semicirculo(entrada_semicirculo): #Se crea una funcion para calcular la inercia y la constante torcional de la figura
    iy_semicir=0.1098*(entrada_semicirculo**4)
    return iy_semicir

def j_semicirculo(entrada_semicirculo):
    j_semicir=0.1098*(entrada_semicirculo**4)*2
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


def ix_sectorcircular (entrada_radio_sector,entrada_angulo_sector): #Se crea una funcion para calcular la inercia y la constante torcional de la figura
    ix_seccir=(entrada_radio_sector**4)*((entrada_angulo_sector)-(math.sin(entrada_angulo_sector)))/8 #Se realizan los calculos para las inercias y la constante torcional (J)
    return ix_seccir

def iy_sectorcircular (entrada_radio_sector,entrada_angulo_sector):
    iy_seccir=(entrada_radio_sector**4)*((entrada_angulo_sector)+(math.sin(entrada_angulo_sector)))/8
    return iy_seccir

def j_sectorcircular (entrada_radio_sector,entrada_angulo_sector):
    j_seccir=((entrada_radio_sector**4)*((entrada_angulo_sector)-(math.sin(entrada_angulo_sector)))/8)+((entrada_radio_sector**4)*((entrada_angulo_sector)+(math.sin(entrada_angulo_sector)))/8)
    return j_seccir

def ix_triangulo (entrada_base_trian,entrada_altura_trian,entrada_a_trian): #Se crea una funcion para calcular la inercia y la constante torcional de la figura
    ix_tri=entrada_base_trian*(entrada_altura_trian**3)/36 #Se realizan los calculos para las inercias y la constante torcional (J)
    return ix_tri

def iy_triangulo (entrada_base_trian,entrada_altura_trian,entrada_a_trian):
    iy_tri=entrada_base_trian*(entrada_altura_trian)*((entrada_a_trian**2)-entrada_a_trian*entrada_base_trian+(entrada_base_trian**2))/36
    return iy_tri

def j_triangulo (entrada_base_trian,entrada_altura_trian,entrada_a_trian):
    j_tri=(entrada_base_trian*(entrada_altura_trian**3)/36)+(entrada_base_trian*(entrada_altura_trian)*((entrada_a_trian**2)-entrada_a_trian*entrada_base_trian+(entrada_base_trian**2))/36)
    return j_tri
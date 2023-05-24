import math #Se importo la libreria math para utilizar funciones matematicas
#Se crean 3 funciones para calcular la inercia y la constante torcional  del rectangulo
#Se realizan los calculos para las inercias y la constante torcional (J)

def ix_rectangulo(entrada_base_rec,entrada_altura_rec): 
    ix_rec=(entrada_base_rec*(entrada_altura_rec**3))/12 
    return ix_rec #se retornan los resultados

def iy_rectangulo(entrada_base_rec,entrada_altura_rec):   
    iy_rec=(entrada_altura_rec*(entrada_base_rec**3))/12
    return iy_rec#se retornan los resultados


def j_rectangulo(entrada_base_rec,entrada_altura_rec):     
    j_rec=((entrada_base_rec*(entrada_altura_rec**3))/12)+((entrada_altura_rec*(entrada_base_rec**3))/12)
    return j_rec#se retornan los resultados

#Se crean 3 funciones para calcular la inercia y la constante torcional  del circulo
#Se realizan los calculos para las inercias y la constante torcional (J)
def ix_circulo(entrada_circulo): 
    ix_cir=((math.pi)*(entrada_circulo**4))/4 
    return ix_cir#se retornan los resultados

def iy_circulo(entrada_circulo): 
    iy_cir=((math.pi)*(entrada_circulo**4))/4
    return iy_cir#se retornan los resultados

def j_circulo(entrada_circulo): 
    j_cir=(((math.pi)*(entrada_circulo**4))/4)+(((math.pi)*(entrada_circulo**4))/4)
    return j_cir#se retornan los resultados

#Se crean 3 funciones para calcular la inercia y la constante torcional  del semicirculo
#Se realizan los calculos para las inercias y la constante torcional (J)
def ix_semicirculo(entrada_semicirculo): 
    ix_semicir=0.1098*(entrada_semicirculo**4) 
    return ix_semicir#se retornan los resultados

def iy_semicirculo(entrada_semicirculo): #Se crea una funcion para calcular la inercia y la constante torcional de la figura
    iy_semicir=0.1098*(entrada_semicirculo**4)
    return iy_semicir#se retornan los resultados

def j_semicirculo(entrada_semicirculo):
    j_semicir=0.1098*(entrada_semicirculo**4)*2
    return j_semicir#se retornan los resultados
    
#Se crean 3 funciones para calcular la inercia y la constante torcional  del cuarto de circulo
#Se realizan los calculos para las inercias y la constante torcional (J)

def ix_cuartodecirculo (entrada_cuartocirculo): 
    ix_cuarcir=0.05488*(entrada_cuartocirculo**4) 
    return ix_cuarcir#se retornan los resultados

def iy_cuartodecirculo (entrada_cuartocirculo):
    iy_cuarcir=0.05488*(entrada_cuartocirculo**4)
    return iy_cuarcir#se retornan los resultados

def j_cuartodecirculo (entrada_cuartocirculo):
    j_cuarcir=0.05488*(entrada_cuartocirculo**4)*2
    return j_cuarcir#se retornan los resultados

#Se crean 3 funciones para calcular la inercia y la constante torcional  del sector circular
#Se realizan los calculos para las inercias y la constante torcional (J)
def ix_sectorcircular (entrada_radio_sector,entrada_angulo_sector): 
    ix_seccir=(entrada_radio_sector**4)*((math.radians(entrada_angulo_sector))-(math.sin(math.radians(entrada_angulo_sector))))/8 
    return ix_seccir#se retornan los resultados

def iy_sectorcircular (entrada_radio_sector,entrada_angulo_sector):
    iy_seccir=(entrada_radio_sector**4)*((math.radians(entrada_angulo_sector))+(math.sin(math.radians(entrada_angulo_sector))))/8
    return iy_seccir#se retornan los resultados

def j_sectorcircular (entrada_radio_sector,entrada_angulo_sector):
    j_seccir=((entrada_radio_sector**4)*((math.radians(entrada_angulo_sector))-(math.sin((math.radians(entrada_angulo_sector)))))/8)+((entrada_radio_sector**4)*(((math.radians(entrada_angulo_sector)))+(math.sin((math.radians(entrada_angulo_sector)))))/8)
    return j_seccir#se retornan los resultados

#Se crean 3 funciones para calcular la inercia y la constante torcional  del sector circular
#Se realizan los calculos para las inercias y la constante torcional (J)
def ix_triangulo (entrada_base_trian,entrada_altura_trian,entrada_a_trian): 
    ix_tri=entrada_base_trian*(entrada_altura_trian**3)/36 
    return ix_tri#se retornan los resultados

def iy_triangulo (entrada_base_trian,entrada_altura_trian,entrada_a_trian):
    iy_tri=entrada_base_trian*(entrada_altura_trian)*((entrada_a_trian**2)-entrada_a_trian*entrada_base_trian+(entrada_base_trian**2))/36
    return iy_tri#se retornan los resultados

def j_triangulo (entrada_base_trian,entrada_altura_trian,entrada_a_trian):
    j_tri=(entrada_base_trian*(entrada_altura_trian**3)/36)+(entrada_base_trian*(entrada_altura_trian)*((entrada_a_trian**2)-entrada_a_trian*entrada_base_trian+(entrada_base_trian**2))/36)
    return j_tri#se retornan los resultados
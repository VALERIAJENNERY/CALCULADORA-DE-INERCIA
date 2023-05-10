import math #Se importo la libreria math para utilizar funciones matematicas

def i_rectangulo(b,h): #Se crea una funcion para calcular la inercia y la constante torcional  de la figura
    ix_rec=(b*(h**3))/12 #Se realizan los calculos para las inercias y la constante torcional (J)
    iy_rec=(h*(b**3))/12
    j_rec=(ix_rec+iy_rec)
    print("El momento de inercia con respecto al eje x es: ", ix_rec, "m\xb3") #Se imprimen los resultados
    print("El momento de inercia con respecto al eje y es: ", iy_rec, "m\xb3")
    print("La constante torcional y es: ", j_rec, "m\xb3")

i_rectangulo(5,2) #Se llama a la función

def i_circulo(r): #Se crea una funcion para calcular la inercia y la constante torcional de la figura
    ix_cir=((math.pi)*(r**4))/4 #Se realizan los calculos para las inercias y la constante torcional (J)
    iy_cir=((math.pi)*(r**4))/4
    j_cir=(ix_cir+iy_cir)
    print("El momento de inercia con respecto al eje x es: ", ix_cir, "m\xb3") #Se imprimen los resultados
    print("El momento de inercia con respecto al eje y es: ", iy_cir, "m\xb3")
    print("La constante torcional y es: ", j_cir, "m\xb3")
i_circulo(2) #Se llama a la función

def i_semicirculo(r): #Se crea una funcion para calcular la inercia y la constante torcional de la figura
    ix_semicir=0.1098*(r**4) #Se realizan los calculos para las inercias y la constante torcional (J)
    j_semicir=(ix_semicir)
    print("El momento de inercia con respecto al eje x es: ", ix_semicir, "m\xb3") #Se imprimen los resultados
    print("La constante torcional y es: ", j_semicir, "m\xb3")
i_semicirculo(2) #Se llama a la función

def i_cuartodecirculo (r): #Se crea una funcion para calcular la inercia y la constante torcional de la figura
    ix_cuarcir=0.05488*(r**4) #Se realizan los calculos para las inercias y la constante torcional (J)
    iy_cuarcir=0.05488*(r**4)
    j_cuarcir=(ix_cuarcir+iy_cuarcir)
    print("El momento de inercia con respecto al eje x es: ", ix_cuarcir, "m\xb3") #Se imprimen los resultados
    print("El momento de inercia con respecto al eje y es: ", iy_cuarcir, "m\xb3")
    print("La constante torcional y es: ", j_cuarcir, "m\xb3")
i_cuartodecirculo (2) #Se llama a la función

def i_sectorcircular (r,an): #Se crea una funcion para calcular la inercia y la constante torcional de la figura
    ix_seccir=(r**4)*((an)-(math.sin(an)))/8 #Se realizan los calculos para las inercias y la constante torcional (J)
    iy_seccir=(r**4)*((an)+(math.sin(an)))/8
    j_seccir=(ix_seccir+iy_seccir)
    print("El momento de inercia con respecto al eje x es: ", ix_seccir, "m\xb3") #Se imprimen los resultados
    print("El momento de inercia con respecto al eje y es: ", iy_seccir, "m\xb3")
    print("La constante torcional y es: ", j_seccir, "m\xb3")
i_sectorcircular (2,30) #Se llama a la función

def i_triangulo (b,h,a): #Se crea una funcion para calcular la inercia y la constante torcional de la figura
    ix_tri=b*(h**3)/36 #Se realizan los calculos para las inercias y la constante torcional (J)
    iy_tri=b*(h**3)*((a**2)-a*b+(b**2))/36
    j_tri=(ix_tri+iy_tri)
    print("El momento de inercia con respecto al eje x es: ", ix_tri, "m\xb3") #Se imprimen los resultados
    print("El momento de inercia con respecto al eje y es: ", iy_tri, "m\xb3")
    print("La constante torcional y es: ", j_tri, "m\xb3")
i_triangulo (2,30,7) #Se llama a la función
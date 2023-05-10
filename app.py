from BACK.areas import * #Se importan los codigos de las funciones para calcular area
from BACK.centroide import * #Se importan los codigos de las funciones para calcular los centroides
from BACK.inercia import * #Se importan los codigos de las funciones para calcular las inercias
from BACK.graficas import * #Se importa el codgico con las funciones para graficar las figuras

figura=input('Seleccione una figura geometrica:') #Se crea un input para la selección de la figura geométrica

if figura == 'RECTANGULO': #Se crea un condicional para figura=rectangulo
    b=float(input('Ingrese la dimensión de la base (m):')) #Se solicita el valor de la base del rectangulo
    h=float(input('Ingrese la dimensión de la altura (m):')) #Se solicita el valor de la altura del rectangulo
    a_rectangulo(b,h) #Se llama a la función de area
    c_rectangulo(b,h) #Se llama a la función de centroide
    i_rectangulo(b,h) #Se llama a la función de inercia
    graficar_rectangulo(b,h) #Se llama a la funcion que grafica la figura

else:
    if figura == 'CIRCULO': #Se crea un condicional para figura=CIRCULO
        r=float(input('Ingrese el valor del radio (m):')) #Se solicita el valor del radio
        a_circulo(r) #Se llama a la función de area
        c_circulo(r)#Se llama a la función de centroide
        i_circulo(r) #Se llama a la función de inercia
        graficar_circulo(r) #Se llama a la funcion que grafica la figura

    else: 
        if figura == 'SEMICIRCULO': #Se crea un condicional para figura=SEMICIRCULO
            r=float(input('Ingrese el valor del radio (m):')) #Se solicita el valor del radio
            a_semicirculo(r) #Se llama a la función de area
            c_semicirculo(r)#Se llama a la función de centroide
            i_semicirculo(r) #Se llama a la función de inercia
            graficar_semicirculo(r) #Se llama a la funcion que grafica la figura

        else:
            if figura == 'CUARTO_DE_CIRCULO': #Se crea un condicional para figura=CUARTO_DE_CIRCULO
                r=float(input('Ingrese el valor del radio (m):')) #Se solicita el valor del radio
                a_cuartodecirculo (r) #Se llama a la función de area
                c_cuartodecirculo (r)#Se llama a la función de centroide
                i_cuartodecirculo (r) #Se llama a la función de inercia
                graficar_cuarto_circulo(r) #Se llama a la funcion que grafica la figura

            else: 
                if figura == 'SECTOR_DE_CIRCULO': #Se crea un condicional para figura=SECTOR_DE_CIRCULO
                    r=float(input('Ingrese el valor del radio (m):')) #Se solicita el valor del radio
                    an=float(input('Ingrese el valor del angulo correspondiente:'))
                    a_sectorcircular (r,an)  #Se llama a la función de area
                    c_sectorcircular (r,an)#Se llama a la función de centroide
                    i_sectorcircular (r,an) #Se llama a la función de inercia
                    graficar_sector(r,an) #Se llama a la funcion que grafica la figura


                else:
                    if figura == 'TRIANGULO': #Se crea un condicional para figura=triangulo
                        b=float(input('Ingrese la dimensión de la base (m):')) #Se solicita el valor de la base del triangulo
                        h=float(input('Ingrese la dimensión de la altura (m):')) #Se solicita el valor de la altura del triangulo
                        a=float(input('Ingrese la dimensión de la distancia a (m):')) #Se solicita el valor de la distancia a
                        a_triangulo (b,h) #Se llama a la función de area
                        c_triangulo (b,h,a) #Se llama a la función de centroide
                        i_triangulo (b,h,a) #Se llama a la función de inercia
                        graficar_triangulo(b,h,a) #Se llama a la funcion que grafica la figura



from BACK.areas import * #Se importan los codigos de las funciones para calcular area
from BACK.centroide import * #Se importan los codigos de las funciones para calcular los centroides
from BACK.inercia import * #Se importan los codigos de las funciones para calcular las inercias

figura=input('Seleccione una figura geometrica:') #Se crea un input para la selección de la figura geométrica

if figura == 'RECTANGULO': #Se crea un condicional para figura=rectangulo
    b=input('Ingrese la dimensión de la base (m)') #Se solicita el valor de la base del rectangulo
    h=input('Ingrese la dimensión de la altura (m)') #Se solicita el valor de la altura del rectangulo
    a_rectangulo(5,2) #Se llama a la función de area
    c_rectangulo(5,2) #Se llama a la función de centroide
    i_rectangulo(5,2) #Se llama a la función de inercia

else:
    if figura == 'CIRCULO': #Se crea un condicional para figura=CIRCULO
        r=input('Ingrese el valor del radio (m)') #Se solicita el valor del radio
        a_circulo(2) #Se llama a la función de area
        c_circulo(2)#Se llama a la función de centroide
        i_circulo(2) #Se llama a la función de inercia

    else: 
        if figura == 'SEMICIRCULO': #Se crea un condicional para figura=SEMICIRCULO
            r=input('Ingrese el valor del radio (m)') #Se solicita el valor del radio
            a_semicirculo(2) #Se llama a la función de area
            c_semicirculo(2)#Se llama a la función de centroide
            i_semicirculo(2) #Se llama a la función de inercia

        else:
            if figura == 'CUARTO_DE_CIRCULO': #Se crea un condicional para figura=CUARTO_DE_CIRCULO
                r=input('Ingrese el valor del radio (m)') #Se solicita el valor del radio
                a_cuartodecirculo (2) #Se llama a la función de area
                c_cuartodecirculo (2)#Se llama a la función de centroide
                i_cuartodecirculo (2) #Se llama a la función de inercia

            else: 
                if figura == 'SECTOR_DE_CIRCULO': #Se crea un condicional para figura=SECTOR_DE_CIRCULO
                    r=input('Ingrese el valor del radio (m)') #Se solicita el valor del radio
                    an=input('Ingrese el valor del angulo correspondiente')
                    a_sectorcircular (2,30)  #Se llama a la función de area
                    c_sectorcircular (2,30)#Se llama a la función de centroide
                    i_sectorcircular (2,30) #Se llama a la función de inercia

                else:
                    if figura == 'RECTANGULO': #Se crea un condicional para figura=triangulo
                        b=input('Ingrese la dimensión de la base (m)') #Se solicita el valor de la base del triangulo
                        h=input('Ingrese la dimensión de la altura (m)') #Se solicita el valor de la altura del triangulo
                        a=input('Ingrese la dimensión de la distancia a (m)') #Se solicita el valor de la distancia a
                        a_triangulo (2,30) #Se llama a la función de area
                        c_triangulo (2,30,7) #Se llama a la función de centroide
                        i_triangulo (2,30,7) #Se llama a la función de inercia


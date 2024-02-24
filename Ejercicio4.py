#Leer la edad de una persona y decir si es mayor o menor de edad

import os
os.system("cls")

def persona():
    edad= int(input("Ingrese su edad"))
    try:
        
        if edad >= 18:
            print ("Sos mayor de edad")
        else:
            print ("Sos menor de edad")
    except:
        print ("Se detecto un problema en el codigo")
persona()       
#Leer la nota de un estudiante y otorgar beca si es mayor a 95%

import os
os.system("cls")

def beca(nota):
     if nota>=95:
         return True
     else:
         return False
nombre= input ("Ingrese su nombre")  
nota_est= float (input("Ingrese su nota:"))

if beca(nota_est):
    print (f"En hora buena {nombre} has conseguido la beca")
else:
    print (f"Lo sentimos {nombre}no has conseguido la beca")
    
   
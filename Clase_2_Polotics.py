print("hello")
print(2+2) #tipo int
print(24e-2) #los float pueden usar notaciones científicas
casa= 2 + 3j #numero + numero seguido de "j" sirve para hacer operaciones con números complejos. No es necesario instalar librerías adicionales. 
print(int(casa.real)) #.real es para ver la parte real de la variable con número complejo
print(int(casa.imag)) #.imag es para ver su parte imaginaria de la variable con número complejo

micadena = "Hola amikos" #tipo string
micadenanumerica = "1234"
print(micadena)
print(float(micadenanumerica)) #para convertir del tipo string al tipo int. con str() convertis a string y con float() a float

variablenueva = "Hola como estan"
print(variablenueva.capitalize()) #para que la variable inicie con mayuscula
print(variablenueva.upper()) #todo en mayuscula
print(variablenueva.lower()) #todo en minuscula

#TRABAJANDO CON FECHAS

#Primero importo la librería

import datetime

#declaramos funciones, variables, o inicializamos

fechadehoy = datetime.datetime.now()
#implementamos la ejecución del operativo

print(fechadehoy)
#type nos dice de que clase es un dato

print(type(fechadehoy))
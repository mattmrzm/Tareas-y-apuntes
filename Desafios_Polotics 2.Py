#Calcular el área de un círculo, dado su radio
import math #para importar el módulo math y usar el valor de pi.
r = int(input("Ingrese el radio: ")) #creo variable r y le pido al usuario que ingrese el radio. lo convierto a numero
print("El área del círculo es de " + str(math.pi * r**2)) #uso la funcion pi de la biblioteca math. convierto el area a texto

#Ingresar numero entero y calcular n + nn + nnn
numero = int(input("Ingrese un número: "))
print(numero + numero**2 + numero**3)

#programa que cuente cadena de caracteres y cuente el tamaño y cuantas veces aparece la letra a, tanto mayus como min
cadena= "A, Mate, cafe, harina, palpito, yerba, mermelada, cacao, picadillo".lower() #.lower() para que cuente a la mayúscula
print("La cantidad de letras de la cadena es de",len(cadena)) #cuenta el tamaño de la cadena
letra_a = 0 #creo la variable que contará la cantidad de letras y la inicializo en 0.
for palabra in cadena: #en cada elemento de la cadena:
  if palabra == "a": #si cada elemento contiene la letra a:
    letra_a=letra_a+1 #el contador de "a" aumentará en uno.
    
print(f"La cantidad de letras 'a' es de: {letra_a}") #muestra la cantidad de letras a luego de que itere por todas las palabras de la cadena. 

#hora actual pero sumar dos horas adicionales
import datetime #porque este módulo debe ser importado
futurahora=int(datetime.time()) #esta función muestra el horario actual. para realizarle cambios a ese horario actual, debo guardar su valor en una variable.
futurahora=futurahora + 2 #a la variable le sumo dos horas
print(futurahora)

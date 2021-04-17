#1 Un programa que imprima "Hola mundo" si a es mayor a b
a = int(input("ingrese el valor de a: ")) #al ponerle el int, si no ingreso un numero arroja un value error.
b = int(input("Ingrese el valor de b: "))

if a > b: 
    print("Hola mundo")
else:
    print("El valor de b es superior al de a")
#2 Un programa que acepte 5 números decimales del usuario:

for i in range(5):
     a=  float(input("Ingrese un número decimal: ")) 

#3 programa que reciba 5 números enteros y l0s guarde en una lista. que recorra la lista y lo muestre en la pantalla



notas= [] #creo la lista
contador= 0 #inicializo el contador
while contador < 5: #para que itere 5 veces
 contador +=1 #y en cada iteración sume 1
 notas.append(int(input("Ingrese su nota: "))) #para agregar un elemento a la lista
for nota in notas: #por cada elemento de la lista
    print(nota) #voy a imprimir el elemento

#4 lista mostrar numeros divisibles por 5 y si encuenta numero mayor a 150 detenga la iteración del bucle

lista1=[12,15,32,42,55,75,122,132,150,180,200]

for i in lista1:
   if i > 150: #luego de 150
       break #el programa se detendrá
   if i % 5 == 0: #si al dividir un elemento por 5 el resto da 0, significa que es divisible por 5-
       print(i) #imprime el valor del elemento
   
    


                 #CADENAS DE CARACTERES
                  
#Son ORDENABLES, pero NO MUTABLES. Un string es una cadena de caracteres,

nombres = "Yanina La Torre" 
print(nombres[0]) #la primera posición se llama posición 0. En este ejemplo, "y". La posicion 1, sería la "a"

                     #LISTAS

#  Son ORDENABLES y MUTABLES.
signos = ["Escorpio", "Piscis"] #se escriben entre corchetes (alt 91 y alt 93) y se separan con comas.
print(signos)
print(signos[1]) #imprime el elemento en la primera posición de la lista
print(signos[1][0]) #de esta forma imprime, del elemento que está en la posición 1 (Piscis), su posición 0 (letra p)

signos.append("Cáncer") #agrega un argumento al final de la cadena. INTENTÉ CON DOS A LA VEZ, NO SE PUEDE. 
print(signos)
signos.sort()
print(signos) #para ordenar la lista. en este caso, alfebticamente

                    #TUPLAS

#ORDENABLES y MUTABLES. En general se utilizan para guardar dos o tres valores, como colores rgb o los de x e y en un plano.
#Llevan paréntesis y se separan con comas.
punto = (12.5,13.3)
print(punto)

                    #SETS (TAMBIÉN LLAMADOS CONJUNTOS)

#NO ORDENABLES y no aplica mutabilidad. A diferencia de listas y tuplas, no puede tener elementos iguales

signosAire = set() #crea el set
signosAire.add("Acuario") #va agregando de a un elemento, no agrega tres a la vez. (similar a append en las listas)
signosAire.add("Cáncer")
signosAire.add("Géminis")
signosAire.add("Acuario") #este valor ya había sido introducido, no lo veremos dos veces. 
signosAire.add("Virgo")#agrego un signo de tierra, ERROR, hay que removerlo
print(signosAire)
signosAire.remove("Virgo") #elimina el elemento
print(signosAire)

print(len(signosAire)) #el len te cuenta la cantidad de elementos, empezando desde el 1. no es como las posiciones
print(len("casa"))#la longitud de casa es de 4 letras
print("casa"[3]) #pero si busco la posición 4 me va a dar un index error(out of range) ya que las 4 letras están en posiciones de 0 a 3.


                        #DICCIONARIOS 
#NO ORDENABLE. MUTABLE. Conjuntos Key Value, cada palabra tiene una definición. se usa llave y dos puntos
#la key va entre corchetes. llaves alt 123 y 125 y corchets 91 y 93.
#para definir un diccionario
zodiaco = {"Cáncer":"Agua", "Acuario" : "Aire", "Leo" : "Fuego", "Virgo" : "Tierra" } #llaves, para crear el diccionario
#imprimir de cual de los cuatro elementos es uno de esos signos:
print(zodiaco["Leo"]) #la key sería leo
#agregar valores a un diccionario
zodiaco["Libra"]="Aire" #le indo que el value aire corresponde a la key libra
print(zodiaco["Libra"])
#OPERADOR TERNARIO DE PYTHON. VALOR CUANDO TRUE IF EXPRESSION ELESE
mivariable = int(input(":"))
print("Es menor") if mivariable<0 else print("es mayor")
#del lado izquierdo expresion si es verdadero y del derecho si es falso.

#for se usa para recorrer muchas veces un bloque de código
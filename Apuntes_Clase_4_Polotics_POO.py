#PROGRAMACION ORIENTADA A OBJETOS


#Objetos = cosa, sustantivo, ej: auto, moto, lancha
#atributos = las propiedades de los objetos. color, ruedas, marca. self.marca
#metodos = comportamientos, funciones. def.
#CLASE
#clase= muchos objetos distintos pueden pertenecer a la misma clase ej:vehiculo
#Se usan para crear los objetos. iNSTANCIACION = Crear un objeto desde una clase
#es una "plantilla" para un nuevo tipo de objeto.

class Fuego: #la clase se escribe en mayusculas, por convención
#en esta parte irian los atributos y comportamientos, pero mientras lo tenga sin rellenar puedo usar PASS como placeholder, así compila sin problemas

                #ATRIBUTOS DE CLASE : Tienen el mismo valor para todas las instancia. se declaran por fuera de init.

    especie = "Pokemon"

#           ATRIBUTOS DE INSTANCIA con Def Init son propiedades que todos los objetos deben tener
    def __init__(self,nombre,descripcion,numero): #define el estado inicial de un objeto asignando valores a las propiedades de esos objetos
        #lo primero que debe pasarse como parámetro es self, el objeto mismo
        self.nombre = nombre
        self.descripcion = descripcion
        self.numero = numero
    #para crearlo dentro de os atributos del propio objeto
#init construye nuestra clase, le ordena como debe inicializarse los atributos/parametros de nuestra clase.



    def  pokedex(self): #si en la funcion en vez de return pongo print, puede salir un None luego del print. en funciones es mejor el return.
        return (f"{self.nombre}, el Pokemon {self.descripcion}, ocupa el lugar número {self.numero} de la pokedex nacional")


    def __str__(self): #cambia el mensaje que se visualiza en consola al llamar a nuestra instancia print(Magmar)
        return f"Este pokemon de tipo fuego es {self.nombre}, {self.descripcion}, ocupa el lugar número {self.numero} de la pokedex nacional "

Magmar = Fuego("Magmar","Escupefuego",126)
 #aca estoy instanciando la clase fuego. paso todos los atributos mens el self
Charmander = Fuego("Charmander","Lagartija",4)
print(Magmar.descripcion) #muestra el atributo descripcion de la instancia magmar
print(type(Magmar)) #me dice que es de la clase Fuego.
print(Magmar.especie) #muestra el atributo de clase general para todas las instancias
print(Magmar.pokedex())
print(Charmander.pokedex())
print(Magmar) #gracias a __str__ se verá un mensaje legible en vez de la posicion de memoria del objeto.
#from Apuntes_Clase_4_Polotics_POO import Fuego para enviar a la terminal

        #HERENCIA
class CharizardRoute(Fuego): #CharizardRoute HEREDA los atributos de su padre Fuego.
    raza = "Charizard" #Aca le agrego el atributo raza, pero tambien puede acceder, a nombre, descripcion, numero, especie

Charmeleon = CharizardRoute("Charmeleon","Lagarto",5)  
print(Charmeleon.pokedex()) #output Charmeleon, el Pokemon Lagarto, ocupa el lugar número 5 de la pokedex nacional
#Ingreso y salida de la terminal:
#>>> from Apuntes_Clase_4_Polotics_POO import CharizardRoute
#>>> Charmeleon = CharizardRoute("Charmeleon","Lagarto",5)  
#>>> type(Charmeleon)
#<class 'Apuntes_Clase_4_Polotics_POO.CharizardRoute'>
#>>> Charmeleon.numero
#5
#>>> Charmeleon.raza
#'Charizard'
#>>> Charmeleon.especie
#'Pokemon'
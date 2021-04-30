#Clase de Python llamada Rectángulo que se defina por una longitud y un ancho y un método que calculará el área

class Rectangulo:
    def __init__(self,longitud,ancho):
        self.longitud = longitud
        self.ancho = ancho
    def Arearectangulo(self):
       print(f"El área del rectángulo es de {self.longitud*self.ancho} metros")     
#from Desafios_Polotics_4_1 import Rectangulo. eso lo pondrìa en la terminal para ingresar datos desde directo desde allà

#Instancio a los rectángulos
rectangulo1= Rectangulo(12,15)
rectangulo2= Rectangulo(4,6)
rectangulo3= Rectangulo(10,10)
#este print muestra el àrea del rectangulo2 segun el metodo Arearectangulo
print(rectangulo2.Arearectangulo())


#BORRADO ICOMPLETO clase Minibus debe heredar de clase vehículo
#metodo capacidad, por defecto de 6 asientos
#crear clase pasajero y agregarla a instancia minibus. Minibus no puede tener mas de 50 pasajeros, ni repetirse

class Vehiculo:
     #pa que no se repitan
    def __init__(self, capacidad=6):
        self.capacidad = capacidad 

    
    

class Minibus(Vehiculo):
    self.asientosocupados = set()
   
minibucito = Minibus("Minibucito S.A", "Volkswagen", 50)
print(minibucito.capacidad)

class Pasajeros:
    def __init__ (self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

pasajero1 = Pasajeros("Juan Perez",18)
pasajero2 = Pasajeros("Marco Antonio",27)
pasajero3 = Pasajeros("Joana Gonzalez",19)
pasajero4 = Pasajeros("Miriam Diaz",11)
print(pasajero3.nombre)

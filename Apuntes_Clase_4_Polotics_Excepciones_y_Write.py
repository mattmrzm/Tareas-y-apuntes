#EXCEPCIONES
#los errores pueden ser tratados mediante excepciones
import sys #para utilizar sys.exit y salir del programa

try: #adentro de try se ponen las líneas de código que se que pueden generar error.
    numero1 = int(input("Ingrese primer numero:") )
    numero2 = int (input("Ingrese segundo numero: "))
except ValueError: #este error ocurre si ingreso un caracter que no sea un numero entero
    print("Ingresó un valor incorrecto")
    sys.exit(1)

try:
    resultado = numero1 / numero2
except ZeroDivisionError: #no se puede dividir un número por zero
    print("Error: No se puede dividir por Zero")
    #Salir del programa
    sys.exit()
else: #se ejecuta si no se produjeron errores
    print("La división fue exitosa")
finally: #visible independientemente de si hubieron errores.
    print("Gracias por elegirnos")
resultado = numero1 / numero2
print (f"{numero1} / {numero2} = {resultado}")

try:
    f = open("miarchivo.txt","w") #al escribir "w", especifico que voy a escribir el archivo. si no aclarara lo de la w, o si tuviera una r, es de solo lectura.
    f.write("Estoy probando a ver si escribe")
except:
    print("No se pudo abrir el archivo")
finally:
    print("Tkm")
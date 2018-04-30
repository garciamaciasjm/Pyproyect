#Ejercicio en el que solicitamos introducir una cadena al usuario, y se van a ir guardando hasta que introduzca una cadena que queramos, entonces, muestra todas las introducidas anteriormente y sale del programa.


def leer(nombre):
    archivo = open(nombre, "r")
    #Es bueno poner la ruta relativa, porque si cambiamos de sistema operativo podemos dejar de acceder al fichero.
    contenido = archivo.read() #lee todo el archivo. Desde la primera posición hasta la última, y la mete en la variable contenido.
    print(type(contenido))
    print(contenido)
    archivo.close()


def ejercicioCadena(nombre):
    archivo = open(nombre, "w+")
    valor=input("Introduce una cadena:")
    while valor != salir:
        archivo.write(str(valor), "\n")
        valor = input("Introduce una cadena:")


def ejerFich1(nombre):
    archivo = open(nombre, "w")
    cadena = input("Introduce cadena:")
    while cadena != "salir":
        archivo.write(cadena+"\n")
        cadena = input("Introduce cadena:")
    archivo.close()
    leer(nombre)


#ejerFich1("cadena")


#Vamos a crear un programa que pida dos variables y van a ser dos ficheros, lo que hay en el primero se tiene que copiar en el segundo.

def escribir(nombre):
    archivo = open(nombre, "w")
    archivo.write("Nueva linea\n")
    archivo.write(str(1))
    archivo.write(str(2))
    archivo.write(str(3))



def copiar(origen, destino):
    archivo1 = open(origen, "r")
    archivo2 = open(destino, "w")
    contenido = archivo1.read()
    archivo2.write(contenido)
    archivo1.close()
    archivo2.close()

copiar("origen")
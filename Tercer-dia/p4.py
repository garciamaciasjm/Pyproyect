

def leer(nombre):
    archivo = open(nombre, "r")
    #Es bueno poner la ruta relativa, porque si cambiamos de sistema operativo podemos dejar de acceder al fichero.
    contenido = archivo.read() #lee todo el archivo. Desde la primera posición hasta la última, y la mete en la variable contenido.
    print(type(contenido))
    print(contenido)
    archivo.close()

def escribir():
    archivo = open(nombre, "w")
    archivo.write("Nueva linea\n")
    archivo.write(str(1))
    archivo.write(str(2))
    archivo.write(str(3))
    '''
    for i in range(10):
        archivo.write(str(i))'''
    archivo.close()

def escribir2(nombre):
    archivo = open(nombre, "w")
    archivo.write("Nueva linea\n")
    for i in range(10):
        archivo.write(str(i))
        archivo.write("\n")
    archivo.close()

def ejemFor():
    #FOREACH
    cadena = "cadena"
    for i in cadena:
        print(i)
    '''
    for i in rage(10): -> Lo que hace es recorrer del 0 al 9 -> 10 valores. si ponemos (11), del 0 al 10 etc etc....
    rage (5,10) -> Va del 5 al 10
    rage (5,50,5)-> Aqui va del 5 al 50(que no llega a imprimirlo porque se queda en el 49) y lo hace de 5 en 5
    '''
    for i in range(20,0-2): #del 20 al cero le va a ir restando dos.
        print(i)

def multiplicar(num):
    for i in range(1,11):
        print(num*i)

def readline(nombre):
    #Lectura de la primera línea del fichero:
    archivo = open("../test.py", "r")
    contenido = archivo.readline()
    print(contenido)
    archivo.close()

def leerArchivo(nombre):
    archivo = open(nombre, "r")
    linea = archivo.readline()
    while linea:
        print(linea, end=".")
        linea = archivo.readline()
    archivo.close()

def leerArchivo2(nombre, num):
    archivo = open(nombre, "r")
    linea = archivo.read(num)
    while linea:
        print("/"+linea+"@")
        linea = archivo.read(num)
    archivo.close()

def ejemSeek(nombre):
    archivo = open(nombre, "r")
    contenido = archivo.read()
    print(contenido)
    archivo.seek(0)

    print("---------")
    contenido = archivo.readline()
    print(contenido)
    archivo.


def ejemTell(nombre):
    archivo = open(nombre, "r")
    print("La posición del cursor es:", archivo.tell())
    archivo.read()
    print("La posición del cursor es:", archivo.tell())
    #print(contenido)
    archivo.seek(0)
    archivo.readline()
    print("La posición del cursor es:", archivo.tell())
    archivo.close()




print("Empezamos programa")
#fichero="/home/jose/Pyproyect/test.py"
#leer("../test.py")

#multiplicar(4)
#escribir2("prueba.py")
#leer("prueba.py")
#readline("prueba.py")
#leerArchivo2("prueba.py", 5)

#ejemSeek("prueba.py")
#ejemTell("prueba.py")

print("Fin programa")
print("Empezamos programa")

cadena = "Ejemplo de cadena"

for i in cadena:
    print(i)

print(len(cadena))
print("------------")
print(cadena[0])
print(cadena[1])
print(cadena[2])

print("------------")

for i in range(len(cadena)):
    print(i,":",cadena[i])

#El intervalo es cerrado por la izquierda, abierto por la derecha, por eso acepta el 2 y el 5 no.

print(cadena[2:5])


#Imprimimos desde el 2 hasta el final:
print(cadena[2:])

#Imprimimos desde el principio hasta el 7
print(cadena[:7])


print("------------")

for i in cadena[2:5]:
    print(i)
print("------------")

#Con números negativos nos recorremos la cadena en sentido contrario:

print(cadena[-2])


for i in range (0,-len(cadena)-1,-1):
    print(i,":", cadena[i])

#print(cadena[-18])

print(cadena[:-1])
print(cadena[:len(cadena)-1])

print("------------")
#Para quitarle la ultima letra a la variable, sería:
cadena = cadena[:-1]


print(cadena.upper())


def ejerFich1(nombre):
    archivo = open(nombre, "w")
    cadena = input("Introduce cadena:")
    while cadena != "salir":
        archivo.write(cadena+"\n")
        cadena = input("Introduce cadena:")
    archivo.close()
    leer(nombre)



def leer(nombre):
    archivo = open(nombre, "r")
    #Es bueno poner la ruta relativa, porque si cambiamos de sistema operativo podemos dejar de acceder al fichero.
    contenido = archivo.read() #lee todo el archivo. Desde la primera posición hasta la última, y la mete en la variable contenido.
    print(type(contenido))
    print(contenido)
    archivo.close()
'''

def ejerFich1(nombre):
    archivo = open(nombre, "w")
    cadena = input("Introduce cadena:")
    while (cadena.upper() != "salir".upper()):
        archivo.write(cadena+"\n")
        cadena = input("Introduce cadena:")
    archivo.close()
    leer(nombre)
'''
ejerFich1(cadena)


def copiar(origen, destino):
    archivo1 = open(origen, "r")
    archivo2 = open(destino, "w")
    linea = archivo1.readline()
    count = 1
    while linea:
        if (count%2 == 0):
            archivo2.write(linea.upper())
        else:
            archivo2.write(linea)
        linea = archivo1.readline()
        count += 1

    archivo1.close()
    archivo2.close()

#copiar("origen")


# Dada una cadena, realiza una busqueda de una subcadena y el número de veces que aparece:
def buscar(cadena, subcadena):
    cont = 0
    pos = cadena.find(subcadena)
    while(pos != -1):
        cont += 1
        pos =cadena.find(subcadena,pos+1,len(cadena))
    return cont


cadena = "Cadena de prueba del curso"
subcadena = "de"



print("Veces:",buscar(cadena, "de"))

print("Finalizamos programa")

#Se continua con los strings en p5.py
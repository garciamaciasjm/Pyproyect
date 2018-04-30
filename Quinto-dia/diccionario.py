import random
#listas en que en cada posición se guarda dos elementos. La posición no es relevante. Si la CALVE(preferiblemente llamado)/Indice para adcceder al valor/Dato o otra lista o otro diccionario.....
#Guarda en memoria en función al HASH del contenido.
#El orden en el que se guardan depende de la clave en la que se está guardando.
#Si asignas un valor ya asignado al diccionario, se elimina el ya existente.
#Creamos el diccionario:
diccionario = {}
diccionario2 = {1:"a", 2:"b", "c":'[1,2,3]'}

print(diccionario2)

#Para imprimir el valor, hay que poner la clave a la que corresponde el valor:

print(diccionario2[1]) # No son posiciones a lo que está imprimiendo sino a las claves.
print(diccionario2[2])
print(diccionario2["c"])
diccionario2[1] = "c" # No son posiciones a lo que apunta sino a las claves.

diccionario = diccionario2 # No crea copia, apunta al la posición en memoria.
diccionario2[3] = "F"

'''
del(diccionario2) -> Te cargas el diccionario entero.
'''
print(diccionario2[3])

print(diccionario2.keys()) #-> Imprime los valores.

#Crea un programa que imprima la clave y el valor a continuación de un diccionario:

def ejer1():
    primero = []
    for i in diccionario2.keys():
        print(i, "->", diccionario2[i])

#Hacer un programa que cree un diccionario con 10 elementos A cada elemento se le van a asignar los primeros numeros 1-10. Y se va a guardar valores cualesquiera en cada uno de ellos.

print("------------------------")



def ejer2():
    diccionario3 = {}
    for i in range(10):
        diccionario3[i] = random.randint(1,30)
        print(diccionario3[i])
        return diccionario3
diccionario3 = ejer2()
print(diccionario3)
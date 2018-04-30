print("Empezamos")

#tupla: lista de variables estática, se define con ()

tupla = (5, 5.3, "hola", 3)
t=3,'a',7
print(type(t),t)

tupla = (6, 5.3, "hola", 3)

print(t[0])
print(t[2])
print("--------")
for i in range(len((t))):
    print(i, t[i])

#no se puede modificar ningun valor de la tupla:

# tupla[0] = 56

#Este es el error que nos mostraría.

#TypeError: 'tuple' object does not support item assignment


#Lista: estructura de datos dynamica. Se define con []

ListaEstaciones = ["Invierno", "Primavera", "Verano", "Otonyo"]

print(ListaEstaciones)
print(ListaEstaciones[0])
print(ListaEstaciones[1])
print(ListaEstaciones[2])

lista2 = [1, 2, 3, [3,4], (8,9)]

for i in lista2:
    print(i, type(i))

print(lista2[4][0]) # Para imprimir la posición cuatro de la lista, y luego la primera de la tupla.

lista2[0] = -1

print(lista2)

lista2[0] = True

#Añadimos elementos al final de la lista:

lista2.append("Muyayo")

print(lista2)

print("-----------------")

#Vamos a crear una lista y la vamos a llenar usando el append con los numeros del 0 al 9

def listaAppend():
    listaAppend1 = []
    for i in range(10):
        listaAppend1.append(i)
    print(listaAppend1)

#listaAppend()

# Importamos una librería para poder usarla:
import random

lista = []
for i in range(10):
    lista.append(random.randint(1,10))
print(lista)

#Generamos dos listas de 10 valores, y una tercera lista ha de contenter los resultados de la primera y la segunda en su posición correspondiente.

def ejer3lista():
    lista1 = []
    lista2 = []
    lista3 = []
    for i in range(10):
        lista1.append(random.randint(1, 10))
    for i in range(10):
        lista2.append(random.randint(1, 10))
    #for i in range(0, len(lista1)):
    for i in range(10):
        lista3.append(int(lista1[i] + int(lista2[i]))) # El int no hace falta porque siempre los va a generar numeros enteros.
    print(lista1)
    print(lista2)
    print(lista3)

print("++++++++++++++++++++++")

#ejer3lista()


nombres = ["Jose", "Miguel", "David"]
print(nombres)
print("Extend es como hacer un \"+\" a lo que ya habia.")
nombres.extend(["Amparo", "Manolo"]) # si en vez de extend hacemos el append, lo que va a hacer es meter una tupla en la posición siguiente con los valores indicados.
print(nombres)
nombres.insert(0, "Dani") #En la posición 0 insterta el valor y los siguientes los desplaza a la derecha.
print(nombres)
nombres.insert(len(nombres), "ultimo")
print(nombres)
nombres.insert(25, "despues del ultimo") # En la posición 25 vamos a meter ese String. Pero no lo hace porque no puede haber posiciones vacias.
print(nombres)

print("-------------------")
lista = [1,2,3,4,5]
lista2 = lista
print(lista)
print(lista2)
lista[2] = 555
print("lista:", lista)
print("lista2:", lista2) # La generada se guarda en memoria, por lo que al crear lista2, apuntamos al mismo sitio en memoria que lista, y si modificamos lista 2, se modifica lista
print("***************")
#para crear una copia de lista:
lista2 = []
for i in lista:
    lista2.append(i)
#lista2.extend(lista) -> Se crea una copia de la lista, de la misma manera que con el for.
print(lista2)
lista2[2] = 777
print(lista2)


print("Fin")
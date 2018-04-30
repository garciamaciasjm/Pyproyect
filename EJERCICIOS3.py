import random

def mostrarMenu():
    print("Bienvendido al programa")
    print("\n")
    print("0. Salir")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Ejercicio 7")
    print("8. Ejercicio 8")
    print("9. Ejercicio 9")
    print("10. Ejercicio 10")


def menu():
    salir = False
    while ( not salir):
        mostrarMenu()
        opcion = input("Seleccione la opción a realizar:")
        if opcion == "0":
            salir = True
        elif opcion == "1":
            ejer1()
        elif opcion == "2":
            ejer2()
        elif opcion == "3":
            ejer3()
        elif opcion == "4":
            ejer4()
        elif opcion == "5":
            ejer5()
        elif opcion == "6":
            ejer6()
        elif opcion == "7":
            ejer7()
        elif opcion == "8":
            ejer8()
        elif opcion == "9":
            ejer9()
        elif opcion == "10":
            ejer10()
        else:
            print("Opción incorrecta")
            input("Pulse cualquier letra:")

# 1. Rellena una lista con los 100 primeros números enteros y muestralos en pantalla en orden ascendente.

def ejer1():
    lista = []
    for i in range(1, 101):
        lista.append(i)
    print(lista)

# 2. Rellena una lista con los 100 primeros números enteros y muestralos en pantalla en orden descendente.

def ejer2():

    lista = []
    for i in range(100, 0, -1):
        lista.append(i)
    print(lista)

# 3. Rellena una lista con los números pares comprendidos entre 1 y 100 y muestralos en pantalla en orden ascendente.

def ejer3():

    inicial = 1
    final = 100
    lista = []
    while inicial <= final:
        if inicial % 2 == 0:
            lista.append(inicial)
            inicial += 1
        else:
            inicial += 1
    print(lista)
# 4. Lea 10 números por teclado, almacenalos en una lista y muestra la suma, resta, multiplicación y división de todos.

def ejer4():
    lista = []
    count = 1
    suma = 0
    resta = 0
    multiplicacion = 1
    division = 1
    while count <= 10:
        numero = int(input("Introduce número:"))
        lista.append(numero)
        count += 1
    for i in range(1, 11):
        suma = lista[i] + suma
        resta = resta - lista[i]
        multiplicacion = lista[i] * multiplicacion
        division = lista[i] / division

    print("La suma es:", suma)
    print("La resta es:", resta)
    print("La multiplicacion es:", multiplicacion)
    print("La division es:", division)

# 5. Lea 5 números por teclado y guardalos en una lista, copialos a otra lista multiplicados por 2 y muestra la segunda lista.

def ejer5():

    lista = []
    lista2 = []
    count = 0

    while count < 5:
        numero = int(input("Introduce número:"))
        lista.append(numero)
        count += 1

    for i in range(0, 5):
        lista2.append(int(lista[i]) * 2)
        print(i)

    print(lista2)
# 6. Representa un tablero de ajedrez en una lista de dos dimendiones y muestrala por pantalla

# peon p
# torre t
# caballo c
# alfil a
# reina r
# rey k
# ' ' (espacio en blanco) para las casillas vacias
# Usa minúsculas para las blancas y mayúsculas para las negras

def ejer6():
    tab = [["t", "c", "a", "r", "k", "a", "c", "t"], ["p", "p", "p", "p", "p", "p", "p", "p"],
           ["0", "0", "0", "4", "0", "0", "0", "0"], ["0", "0", "0", "4", "0", "0", "0", "0"],
           ["0", "0", "0", "4", "0", "0", "0", "0"], ["0", "0", "0", "4", "0", "0", "0", "0"],
           ["0", "0", "5", "5", "5", "5", "5", "0"], ["0", "0", "0", "0", "9", "9", "9", "9"],
           ["p", "p", "p", "p", "p", "p", "p", "p"], ["t", "c", "a", "r", "k", "a", "c", "t"]]

    return (tab)
# 7. Implementa el movimiento de los peones del tablero

def ejer7():

# 8. Implementa un programa que reciba dos números como argumentos. El primero indicará el tamaño de una lista que tendrá que crearse y rellenar con números aleatorios NO REPETIDOS, con valores comprendidos entre 1 y el segundo parámetro. Una vez rellenada la lista, el programa la mostrará por pantalla.
# Ejemplo de utilización:
# >python programa.py 6 20
# 3 7 14 17 19 2
    tab = ejer6()
    mostrar(tab)
    peon = input("Introduzca columna del peon que quiere mover, o salir si quiere detener el juego")
    fila = 0
    columna = 0
    turno = 1
    contador = 1
    tab = ejercicio6()
    mostrar(tab)
    while peon != "salir":
        if contador % 2 != 0:

            peon = int(peon)
            print("-------")
            tab[6][peon - 1] = "0"
            tab[5][peon - 1] = "p"
            mostrar(tab)
            print("-------")
            peon = input("Introduzca columna del peon que quiere mover, o salir si quiere detener el juego")
        else:
            peon = int(peon)
            print("-------")
            tab[1][peon - 1] = "0"
            tab[2][peon - 1] = "p"
            mostrar(tab)
            print("-------")
            peon = input("Introduzca columna del peon que quiere mover, o salir si quiere detener el juego")
        contador += 1

    print(tab)


def ejer8():
    import random
    y = int(input("Inserta el tamaño de la lista:"))
    x = int(input("Inserta hasta el valor numérico que quieres de la lista"))
    lista = []
    valor = ""

    while (int(len(lista)) < y):
        valor = random.randint(1, x)
        while valor in lista:
            valor = random.randint(1, x)
        lista.append(valor)

    print(lista)


# 9. Implementa un programa que reciba como argumentos un conjunto C de palabras y un número N como último argumento. El programa tendrá que generar N palabras aleatorias de entre las introducidas en C.
# Por ejemplo:
# >palabrasAleatorias.py uno dos tres cuatro cinco seis 4
# cuatro seis uno seis
# Fin

def ejer9():

    lista = []
    lista2 = []
    estado =True

    while estado == True:
        introducido = input("Teclee una lista de palabras y finalmente un numero")

        if introducido.isdigit() == False:
            lista.append(introducido)
        else:
            a = False
            numero = int(introducido)
    print("lista de palabras introducidas", lista)
    print("longitud", len(lista))

    contador = 1
    while (contador <= numero):
        al = random.randint(1, len(lista))
        lista2.append(lista[al - 1])
        contador += 1
    print("palabras aleatorias", lista2)


# 10. Implementa el ejercicio anterior pero con la restricción de que las palabras generadas no puedan repetirse. Si el número introducido excede el número de palabras introducidas, entonces el programa generará tantas palabras como le sea posible sin repetir ninguna.
# Ejemplo:
# >palabrasAleatorias.py uno dos tres cuatro cinco seis 7
# cuatro seis uno dos cinco tres
# Fin

def ejer10():
    estado = True
    lista = []
    lista2 = []
    while estado == True:
        introducido = input("Inserta una palabra y al final un número")

        if introducido.isdigit() == False:
            lista.append(introducido)
        else:
            # if introducido.isdigit()==True:
            estado = False
            numerointroducido = int(introducido)
    print("lista de palabras introducidas", lista)
    print("longitud", len(lista))

    listanumeros = []

    contador = 0
    while contador < len(lista):
        estado = False
        while estado == False:
            numero = random.randint(1, len(lista))
            estado = True
            for te in listanumeros:
                if numero == te:
                    estado = False
        listanumeros.append(numero)
        contador += 1
    print("listanumeros", listanumeros)
    contador = 0
    while (contador < numerointroducido and contador < len(lista)):
        lista2.append(lista[listanumeros[contador] - 1])
        contador += 1
    print("palabras aleatorias", lista2)
menu()



'''

Vamos a generar un programa para gestionar los datos de un concesionario con las siguientes funcionales:

1. Alta
2. Baja
3. Modificacion
4. Busqueda
5. Mostrar todos
0. Salir.
'''
# while not salir se podría haber hecho para repetir siempre el menu:
def mostrarMenu():
    print("Bienvendido al programa")
    print("\n")
    print("Estas son las funciones que puedes realizar:")
    print("\n")
    print("0. Salir")
    print("1. Alta")
    print("2. Baja")
    print("3. Modificacion")
    print("4. Busqueda")
    print("5. Mostrar todos")

def menu():
    biblioteca = {}
    salir = False
    while ( not salir):
        mostrarMenu()
        opcion = input("Seleccione la opción a realizar:")
        if opcion == "0":
            salir = True
        elif opcion == "1":
            alta(biblioteca)
        elif opcion == "2":
            baja(biblioteca)
        elif opcion == "3":
            modificacion(biblioteca)
        elif opcion == "4":
            busqueda(biblioteca)
        elif opcion == "5":
            mostrartodos(biblioteca)
        else:
            print("Opción incorrecta")
            input("Pulse cualquier letra:")



def alta(biblioteca):
    matricula = input("Introduzca matricula")
    datos = [input("Introduzca marca"), input("Introduzca modelo"), input("Introduzca color")]
    biblioteca[matricula] = datos
    #return biblioteca

def baja(biblioteca):
    baja = input("Introduzca la matricula a eliminar:")
    del(biblioteca[baja])


def modificacion(biblioteca):
    matricula = input("Introduzca matricula")
    #datos = [input("Introduzca marca"), input("Introduzca modelo"), input("Introduzca color")]
    biblioteca[matricula] = [input("Introduzca marca"), input("Introduzca modelo"), input("Introduzca color")]
    #biblioteca = {matricula: datos}


def busqueda(biblioteca):
    matricula = input("Introduzca matricula")
    #for matricula in biblioteca: # se puede poner if "algo" not in "dato complejo (tupla,lista,biblioteca....)"
    print(biblioteca[matricula])
    menu()

def mostrartodos(biblioteca):
    for i in biblioteca.keys():
        print(i, "->", biblioteca[i])



menu()

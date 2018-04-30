import sqlite3


def mostrarMenu():
    print("Bienvendido al programa")
    print("\n")
    print("1. Alta")
    print("2. Baja")
    print("3. Buscar alumnos")
    print("4. Modificar")
    print("5. Mostrar todos")
    print("0. Salir")


def menu():
    salir = False
    while ( not salir):
        mostrarMenu()
        opcion = input("Seleccione la opción a realizar:")
        if opcion == "0":
            cerrarbbdd()
            salir = True
        elif opcion == "1":
            alta()
        elif opcion == "2":
            baja()
        elif opcion == "3":
            buscar()
        elif opcion == "4":
            modificar()
        elif opcion == "5":
            mostrar()
        else:
            print("Opción incorrecta")
            input("Pulse cualquier letra:")


def conectarbbdd(fich):
    connection = sqlite3.connect(fich)

    cursor = connection.cursor()
    return cursor

def mostrar():
    cursor.execute("SELECT * FROM alumnos")
    registros = cursor.fetchall()  # devuelve todos los valores y recorro toda la lista.
    print(type(registros))
    for registro in registros:
        print(registro, type(registro))
    connection.

def alta():

    respuesta = input("Inserta 'A' para insertar un alumno, o 'P' para insertar un profesor")

    while not (respuesta == "A" or respuesta == "P"):
        respuesta = input("Inserta 'A' para insertar un alumno, o 'P' para insertar un profesor")

    if respuesta == "A":

        a = input("Inserta el nombre del alumno:")
        b = input("Inserta el nombre del apellido:")
        c = input("Inserta el nombre del dirección:")
        d = input("Inserta el nombre del teléfono:")
        e = input("Inserta el numero del expediente:")
        print(a, b, c, d, e)

        print("INSERT INTO alumnos VALUES (NULL, '"+a+"', '"+b+"', '"+c+"', '"+d+"', '"+e+"')")

        comando1 = "INSERT INTO alumnos VALUES (NULL, '"+a+"', '"+b+"', '"+c+"', '"+d+"', '"+e+"')"
        cursor.execute(comando1)
        connection.commit()

    else:

        a = input("Inserta el nombre del Profesor:")
        b = input("Inserta el nombre del apellido:")
        c = input("Inserta el nombre del dirección:")
        d = input("Inserta el nombre del teléfono:")
        e = input("Inserta el numero del seguridad social:")

        connection = conectarbbdd()
        comando1 = "INSERT INTO profesores VALUES (NULL, '" +str(a)+ "', '" + str(b) + "', '" + str(c) + "', '" + str(d) + "', '" + str(e) + "')"
        cursor.execute(comando1)
        connection.commit()


bbdd = 'Colegio.sqlite'
cursor = conectarbbdd(bbdd)
print("***********************************")

menu()




'''
Se tiene que guardar en una BBDD.

MENU:
1. ALTA
2. BAJA
3. BUSCAR ALUMNOS
4. MODIFICAR
5. MOSTRAR TODOS
0. SALIR
INTRO OPCION

Alumnos: numero expediente.

Profesores: numero seguridad social.

'''
import sqlite3
def mostrarMenu():

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



def cerrarbbdd():
    cursor.close()
    connection.close()


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

        comando1 = "INSERT INTO alumnos VALUES ('"+a+"', '"+b+"', '"+c+"', '"+d+"', '"+e+"')"
        cursor.execute(comando1)
        connection.commit()

    else:

        a = input("Inserta el nombre del Profesor:")
        b = input("Inserta el nombre del apellido:")
        c = input("Inserta el nombre del dirección:")
        d = input("Inserta el nombre del teléfono:")
        e = input("Inserta el numero del seguridad social:")

        comando1 = "INSERT INTO profesores VALUES ('"+a+"', '"+b+"', '"+c+"', '"+d+"', '"+e+"')"
        cursor.execute(comando1)
        connection.commit()

def baja():

    respuesta = input("Inserta 'A' para eliminar un alumno, o 'P' para eliminar un profesor")

    while not (respuesta == "A" or respuesta == "P"):
        respuesta = input("Inserta 'A' para eliminar un alumno, o 'P' para eliminar un profesor")

    if respuesta == "A":
        alpro = "alumnos"

    else:
        alpro = "profesores"

    try:
        exit = False
        while (not exit):

            submenu()
            opcion = input("Seleccione el campo por el que quiere eliminar:")

            if opcion == "1":

                bus = input("Inserta el nombre a eliminar: ")
                cursor.execute("DELETE from "+alpro+" WHERE nombre='" + bus + "';")
                registros = cursor.fetchall()

                for registro in registros:
                    print(registro)

                exit = True

            elif opcion == "2":

                bus = input("Inserta el apellido a eliminar: ")
                cursor.execute("DELETE from "+alpro+" WHERE apellidos='" + bus + "';")
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)

                exit = True

            elif opcion == "3":

                bus = input("Inserta direccion a eliminar: ")
                cursor.execute("DELETE from "+alpro+" WHERE direccion='" + bus + "';")
                registros = cursor.fetchall()

                for registro in registros:
                    print(registro)

                exit = True

            elif opcion == "4":

                bus = input("Inserta el telefono a eliminar: ")
                cursor.execute("DELETE from "+alpro+" WHERE telefono='" + bus + "';")
                registros = cursor.fetchall()

                for registro in registros:
                    print(registro)

                exit = True

            elif opcion == "5":

                bus = input("Inserta el expediente a eliminar: ")
                cursor.execute("DELETE from "+alpro+" WHERE expediente='" + bus + "';")
                registros = cursor.fetchall()

                for registro in registros:
                    print(registro)

                exit = True

            else:
                print("Opción incorrecta")
                input("Pulse cualquier letra:")

    except sqlite3.OperationalError as error:
        print("Valor introducido incorrecto:", error)



def mostrar():

    print('\n',"Detallamos la lista de profesores: ",'\n')

    cursor.execute("SELECT * FROM profesores")
    registros1 = cursor.fetchall()

    for registro in registros1:
        print(registro)

    print('\n',"Detallamos la lista de alumnos: ",'\n')

    cursor.execute("SELECT * FROM alumnos")
    registros2 = cursor.fetchall()

    for registro in registros2:
        print(registro)


def submenu():

    print("\n")
    print("1. nombre")
    print("2. apellido")
    print("3. direccion")
    print("4. telefono")
    print("5. expediente")

def submenu1():

    print("\n")
    print("1. nombre")
    print("2. apellido")
    print("3. direccion")
    print("4. telefono")

def buscar():

    try:

        exit = False
        while ( not exit):

            submenu()
            opcion = input("Seleccione el campo por el que quiere buscar:")

            if opcion == "1":
                bus = input("Inserta el nombre a buscar: ")
                cursor.execute("SELECT * from alumnos WHERE nombre='" + bus + "';")
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)
                exit = True

            elif opcion == "2":

                bus = input("Inserta el apellido a buscar: ")
                cursor.execute("SELECT * from alumnos WHERE apellidos='" + bus + "';")
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)
                exit = True

            elif opcion == "3":

                bus = input("Inserta direccion a buscar: ")
                cursor.execute("SELECT * from alumnos WHERE direccion='" + bus + "';")
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)
                exit = True

            elif opcion == "4":

                bus = input("Inserta el telefono a buscar: ")
                cursor.execute("SELECT * from alumnos WHERE telefono='" + bus + "';")
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)
                exit = True

            elif opcion == "5":

                bus = input("Inserta el expediente a buscar: ")
                cursor.execute("SELECT * from alumnos WHERE expediente='" + bus + "';")
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)
                exit = True

            else:
                print("Opción incorrecta")
                input("Pulse cualquier letra:")

    except sqlite3.OperationalError as error:
        print("Valor introducido incorrecto:", error)

def modificar():

    respuesta = input("Inserta 'A' para modificar un alumno, o 'P' para modificar un profesor")

    while not (respuesta == "A" or respuesta == "P"):
        respuesta = input("Inserta 'A' para modificar un alumno, o 'P' para modificar un profesor")

    if respuesta == "A":
        alpro = "alumnos"
        campo = "expediente"
        result = input("Inserte el número de expediente del alumno a modificar: ")

    else:
        alpro = "profesores"
        campo = "ss"
        result = input("Inserte el número de la seguridad social del profesor a modificar: ")

    try:
        exit = False
        while (not exit):

            submenu1()
            opcion = input("Seleccione el campo por el que quiere modificar:")

            if opcion == "1":

                bus = input("Inserta el nombre a que quieres introducir: ")
                cursor.execute("UPDATE "+alpro+" set nombre='" + bus + "' WHERE "+ campo +"='"+ result +"';")
                registros = cursor.fetchall()

                for registro in registros:
                    print(registro)

                exit = True

            elif opcion == "2":

                bus = input("Inserta el apellido a modificar: ")
                cursor.execute("UPDATE " + alpro + " set apellido='" + bus + "' WHERE " + campo + "='" + result + "';")
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)

                exit = True

            elif opcion == "3":

                bus = input("Inserta direccion a modificar: ")
                cursor.execute("UPDATE " + alpro + " set direccion='" + bus + "' WHERE " + campo + "='" + result + "';")
                registros = cursor.fetchall()

                for registro in registros:
                    print(registro)

                exit = True

            elif opcion == "4":

                bus = input("Inserta el telefono a modificar: ")
                cursor.execute("UPDATE " + alpro + " set telefono='" + bus + "' WHERE " + campo + "='" + result + "';")
                registros = cursor.fetchall()

                for registro in registros:
                    print(registro)

                exit = True

            else:
                print("Opción incorrecta")
                input("Pulse cualquier letra:")

    except sqlite3.OperationalError as error:
        print("Valor introducido incorrecto:", error)



print("Bienvendido al programa")

connection = sqlite3.connect('Colegio.sqlite')

cursor = connection.cursor()

menu()

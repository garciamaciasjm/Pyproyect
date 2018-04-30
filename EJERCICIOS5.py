'''

Se tiene que guardar en un fichero.


MENU:
1. ALTA
2. BAJA
3. BUSCAR ALUMNOS
4. MODIFICAR
5. MOSTRAR TODOS
0. SALIR
INTRO OPCION

Persona: nombre, apellidos, dir, tele.
+
Alumnos: numero expediente.

Profesores: numero seguridad social.

**Hay que añadir un primer campo para identificar si es alumno o profesor. Para mostrarlos, y para borrar.
**Se lee del fichero, se carga en memoria, y despues se vuelve a grabar en el fichero, nunca se trabaja sobre el fichero directamente.
'''

class Persona():
    persona = 0
    def __init__(self, alpro, nombre, apellido, direccion, telefono):
        self.alpro = alpro
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.id = Persona.persona
        Persona.persona += 1

    def __str__(self):
        return self.alpro+","+self.nombre+","+self.apellido+","+self.direccion+","+self.telefono

    def to_string(self):
        result = "Nombre: " + self.nombre + "\n"
        result = result + "Apellido: " + self.nombre + "\n"
        result = result + "Direccion: " + self.direccion + "\n"
        return result
        # return self.alpro+","+self.nombre+","+self.apellido+","+self.direccion+","+self.telefono


class Alumno(Persona):

    def __init__(self, nombre, apellido, direccion, telefono, expediente):
        super().__init__("alumno", nombre, apellido, direccion, telefono)
        self.expediente = expediente

    def __str__(self):
        return super().__str__()+","+self.expediente


class Profesores(Persona):

    def __init__(self, nombre, apellido, direccion, telefono, ss):
        super().__init__("profesor", nombre, apellido, direccion, telefono)
        self.ss = ss

    def __str__(self):
        return super().__str__()+","+self.ss

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
            guardarAgenda(agenda, fichero)
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


def cargaAgenda(agenda, fich):
    archivo = open(fich, "r")
    linea = archivo.readline()

    while linea:
        if (linea[-1] =="\n"):
            linea = linea[:-1]
        campos = linea.split(",")
        if (len(campos) >= 6):

            if(campos[0] == "profesor"):
                p = Profesores(campos[1], campos[2], campos[3], campos[4], campos[5])
                agenda.append(p)
            elif (campos[0] == "alumno"):
                p = Alumno(campos[1], campos[2], campos[3], campos[4], campos[5])
                agenda.append(p)

        linea = archivo.readline()



def guardarAgenda(agenda, fich):
    archivo = open(fich, "w")
    for i in agenda:
        archivo.write(i.__str__())

        archivo.write("\n")
    archivo.close()

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

        p = Alumno(a, b, c, d, e)
        agenda.append(p)

    else:

        a = input("Inserta el nombre del Profesor:")
        b = input("Inserta el nombre del apellido:")
        c = input("Inserta el nombre del dirección:")
        d = input("Inserta el nombre del teléfono:")
        e = input("Inserta el numero del seguridad social:")

        p = Profesores(a, b, c, d, e)
        agenda.append(p)

def baja():

    mostrar()
    baja = int(input("Introduzca el 'id' de la persona a eliminar: "))

    try:
        for i in range(0, len(agenda)):
            if agenda[i].id == baja:
                del(agenda[i])
                break

    except IndexError as error:

     print("ID incorrecto:", error)



def mostrar():

    for persona in agenda:
        print(persona.id, persona.__str__())


def buscar():

    bus = input("Introduce el parámetro a buscar")

    for person in agenda:
        if person.alpro == "alumno":
            if (bus == person.nombre or bus == person.apellido or bus == person.direccion or bus == person.telefono):
                print(person.__str__())



def modificar():

    if (len(agenda) < 0):
        print("No hay personas para modificar.")
    else:
        mostrar()
        insertedId = int(input("Introduzca el 'id' de la persona a editar: "))

        try:
            for i in range(0, len(agenda)):
                print(agenda[i].id)
                if agenda[i].id == insertedId:

                    p = agenda[i]
                    var1 = input("Inserta el nombre:")
                    if var1 != "":
                        p.nombre = var1

                    var1 = input("Inserta el apellido:")
                    if var1 != "":
                        p.apellido = var1

                    var1 = input("Inserta el dirección:")
                    if var1 != "":
                        p.direccion = var1

                    var1 = input("Inserta el teléfono:")
                    if var1 != "":
                        p.telefono = var1

                    if p.alpro == "alumno":

                        var1 = input("Inserta el expediente:")
                        if var1 != "":
                            p.expediente = var1

                    elif p.alpro == "profesor":

                        var1 = input("Inserta el nombre de la ss:")
                        if var1 != "":
                            p.ss = var1

                    agenda[i] = p
                    break

        except IndexError as error:

            print("ID incorrecto:", error)


agenda = []
fichero = "agenda.txt"
cargaAgenda(agenda, fichero)

menu()

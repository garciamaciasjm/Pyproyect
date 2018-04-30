import random

#vamos a crear una clase llamado personas con un metodo que haga algo ademas del contructor y el str y el destructor, y creamos 10 personas. y atributos nombre apellidos direccion y teléfono.

class Contactos():
    contactos = 0
    def __init__(self, nombre, apellidos, direccion, telefono): #Si pusieramos name ="", no seria un requisito obligatorio, ya que se le asigna un valor nulo si no se mete nada, por defecto.
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        Contactos.contactos += 1

    def __str__(self):
        return "Contacto :"+self.nombre+","+self.apellidos+","+self.direccion+","+self.telefono

    def __del__(self):
        print("Destriumos a", self.nombre)

    def salta(self):
        print(self.nombre, "salta")

def cargaAgenda(agenda, fich):
    archivo = open(fich, "r")
    linea = archivo.readline()
    while linea:
        if (linea[-1] =="\n"):
            linea = linea[:-1] # para que no meta el salto de linea en cada campo. Que es el ultimo caracter.
        campos = linea.split(",")
        if (len(campos)=='4'):
            p = Contactos(campos[0], campos[1], campos[2], campos[3])
            agenda.append(p)
        linea = archivo.readline()

def guardarAgenda(agenda, fich):
    archivo = open(fich, "w")
    for i in agenda:
        archivo.write(i.__str__()) # se podría poner al final objeto.nombre|apelllidos ....
        archivo.write("\n")
    archivo.close()

agenda = []
fichero = "agenda.txt"
cargaAgenda(agenda,fichero)


for i in range(10):
    p = Contactos("nom_"+str(i), "ape_"+str(i), "dir_"+str(i), "tel_"+str(i))
    agenda.append(p)

for i in agenda:
    print(i)

for i in agenda:
    i.salta()


for _ in range(5):
    pos = random.randint(0,len(agenda)-1)
    agenda[pos].salta()

guardarAgenda(agenda, fichero)


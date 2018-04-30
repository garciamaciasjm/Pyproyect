class Clase1():
    # Init se refiere a constructor especial. con el que creamos los atributos.
    def __init__(self, name, salary=0): #Si pusieramos name ="", no seria un requisito obligatorio, ya que se le asigna un valor nulo si no se mete nada, por defecto.
        print("Creamos un objeto Clase1:",name)
        self.name = name
        self.salary = salary #si le pasamos el nombre Ana a la clase, self se referirá a Ana, para definir su salario y su nombre.

    def __str__(self):
        return "Clase1:"+self.name

    def __del__(self):
        print("Destriumos a", self.name)

class Clase2():

    def __init__(self):
        self.at1 = 1
        self.at2 = 'valor'

pepe = Clase2
pepe.at1 = 2

print("Empezamos")
print("-")
c1 = Clase1("Ana")
print("-")
c2 = Clase1("Juan")
print("-")
c3 = Clase1("Jose", 5000)
print("-")
print(1,c1.name,c1.salary)
print(2,c2.name,c2.salary)
print(3,c3.name,c3.salary)

print(4,c3)
print("-"*25)
c1 = 5


class Clase1():
    empCount = 0#Estaticos o de clase

    def __init__(self, name="", salary=0):
        self.name = name
        self.salary = salary
        Clase1.empCount += 1
   
    def displayCount(self):
        print("Total Employee %d", clase1.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)
        
    def __del__(self):
        class_name = self.__class__.__name__ #Se ha borrado un nombre de clase 1
        print(class_name, "destroyed")
        
    def __str__(self):
        return "blabla"+self.name+" "+str(self.salary)


class Clase2:
    num=1
    num2=2
    num3=3
    

print("Begin")

clasePrueba = Clase1()
clasePrueba2 = Clase2()

print(clasePrueba)
print(clasePrueba2)

"""This would create first object of Employee class"""
emp1 = Clase1("Zara", 2000)
"This would create second object of Employee class"
emp2 = Clase1("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee", Clase1.empCount)
print("Total Employee", emp2.empCount)
print("Total Employee", emp1.empCount)
emp1.empCount=0 # Se le asigna un valor a traves de los atributos
emp2.empCount=1 # Se le asigna un valor a traves de los atributos
print("Total Employee", emp1.empCount)# Se está creando un atributo asociado a un objeto, Y ESTO NO SE DEBE DE HACER. SE DEBE DE HACER EN EL CONTRUCTO
print("Total Employee", emp2.empCount) # LO MISMO
print("Total Employee", Clase1.empCount) # LO MISMO.

print("----------------")
a1=Clase2()
a1.num=11
a1.num2=22
Clase2.num3=33
a2=Clase2()
print(a1.num)
print(a1.num2)
print(a1.num3)
print(a2.num)
print(a2.num2)
print(a2.num3)
print("----Clase")
#Si cambiamos el atributo de la clase se modifica en todos
Clase2.num3=500
print(a1.num3)
print(a2.num3)
print(Clase2.num3)
print("----A1")
a1.num3=55
#Al cambiar el atributo de un objeto, este se desvincula
print(a1.num3)
print(a2.num3)
print(Clase2.num3)
print("----Clase")
Clase2.num3=505
#Al cambiar el atributo de la clase vemos que a2 sigue vinculado
print(a1.num3)
print(a2.num3)
print(Clase2.num3)
print("----A2")
a2.num3=66
#Desvinculamos a2
print(a1.num3)
print(a2.num3)
print(Clase2.num3)
print("----Clase")
Clase2.num3=77
#Ahora solo se modifica la clase
print(a1.num3)
print(a2.num3)
print(Clase2.num3)

print("+++++++++++++++++++")
print(emp1.name)
print(emp2.name)
#print(clase1.name) #ERROR. Al definirlo de la otra forma no pertenece a la clase
print("++++")
Clase1.name="Nombre de clase"
print(emp1.name)
print(emp2.name)
print(Clase1.name)

Clase1.name2blabla="Nombre de clase2"
print(Clase1.name2blabla)
emp1.nom34=5
#print(emp1.nom34)
#print(emp2.nom34)


print("Fin")

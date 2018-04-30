#Herencia de atributos y metodos de una clase a otra
#Se puede heredar es de mas clases, aunque lo correcto es heredar sólo de una.

class Animal():
    def __init__(self, id, nombre):	
        self.id = id
        self.nombre = nombre
    def pintar(self):
        print("Animal")
    
class clase2():
    def mostrar(self,mensaje):
        print("clase2:",mensaje)
    def pintar(self):
        print("Clase2")
        
        
class Ave(clase2,Animal): # Si hay un conflicto al heredar un metodo, prevalece el primero que usas, en este caso "clase2"
    def __init__(self, id, nombre, peso): # Init crea los atributos de los objetos.
        super().__init__(id,nombre) # Para referirnos a la clase de la que heredas. Si se hereda de más, dependerá de los parámetros que le metas (que coincida -> En este caso id y nombre.)
        #self.id = id
        #self.nombre = nombre
        self.peso = peso
        

paj = Ave(1,"ave1",45)
print("----------")
paj.pintar()
print("----------")

pajaro1=Ave(2,"ave2",75)
print(pajaro1.id)
print(pajaro1.nombre)
print(pajaro1.peso)
pajaro1.mostrar("mensaje")
pajaro2=Ave(3,"ave3",21)

pajaro1.alas=2
print(pajaro1.alas)
#print(pajaro2.alas)
#print(Ave.alas)

Ave.alas = 4
print(pajaro2.alas)
print(pajaro1.alas)
print(Ave.alas)


#Mirar UML para definir las clases y la relacion que va a tener con otras y sus herencias

#Las clases de agrupan en librerias
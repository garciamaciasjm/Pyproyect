class Persona(): #Siempre ha de empezar por mayúsculas
    nombre =""
    direccion =""
    padre = ""

    def saltar(self):
        print(self.nombre, "Salta")


print("Empezamos")

obj_juan = Persona()
obj_juan.nombre = "Juan"
obj_juan.direccion = "Madrid"
print(obj_juan.nombre, "-", obj_juan.direccion)


p2 = Persona()
p2.nombre = "Jose"
p2.direccion = "Barcelona"
print(p2.nombre, "-", p2.direccion)

p2.saltar()

p2.padre = obj_juan
obj_juan.saltar()
p2.padre.saltar()


print("Fin")
import random

class Vehiculo():

    def __init__(self, matricula, marca, modelo, color):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return self.matricula+", "+self.marca+", "+self.modelo+", "+self.color

class Moto(Vehiculo):

    def __init__(self, matricula, marca, modelo, color):
        super().__init__(matricula, marca, modelo, color)

    def __str__(self):
        return "Moto: "+super().__str__()

class Coche(Vehiculo):

    def __init__(self, matricula, marca, modelo, color, plazas):
        super().__init__(matricula, marca, modelo, color)
        self.plazas = plazas

    def __str__(self):
        return "Coche: "+super().__str__()+", "+self.plazas

class Camion(Vehiculo):

    def __init__(self, matricula, marca, modelo, color, carga):
        super().__init__(matricula, marca, modelo, color)
        self.carga = carga

    def __str__(self):
        return "Camion: "+super().__str__()+", "+self.carga

motos = []
coches = {}
camion = {}

for i in range(10):
    a = Moto("matr_"+str(i), "marca_"+str(i), "modelo_"+str(i), "color_"+str(i))
    motos.append(a)

for i in motos:
    print(i)

for i in range(10):
    v = Coche("matr_"+str(i), "marca_"+str(i), "modelo_"+str(i), "color_"+str(i), "plazas_"+str(3+random.randint(0, 5)))
    coches["mat_"+str(i)] = v

for i in coches.keys():
    print(coches[i])


for i in range(10):
    c = Camion("matr_"+str(i), "marca_"+str(i), "modelo_"+str(i), "color_"+str(i), "carga_"+str(i))
    camion["mat_"+str(i)] = c

for i in camion.keys():
    print(camion[i])


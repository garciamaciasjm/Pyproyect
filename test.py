# variable1 = input("Inserte una letra en minúsculas y te diré si es vocal:")
# x = True
# y = False
#
# if ():
#
# if((variable1 =="a") or (variable1 =="e")or (variable1 =="i")or (variable1 =="o")or (variable1 =="u")):
#     print("La letra", variable1,"es una vocal")
# else:
#     print("La letra es una consonante")
'''
def x():
    print("x")
    return True

def y():
    print("y")
    return False


if (x() & y()):
    print("end")

def f():
    global s
    print(s)
    s = "dog"
    print(s)
s = "cat"
f()
print(s)

print("-------------")

def jose(archivo1, archivo2):
    file1 = open(archivo1, "r")
    file2 = open(archivo2, "w")

    for i in file1.readlines():
        file2.write(i)

    file1.close()
    file2.close()

    print("Lineas copiadas")


jose("fichero", "destino")
'''

def leer(nombre):
    archivo = open(nombre, "r")
    contenido_archivo = archivo.read()
    print(contenido_archivo, type(contenido_archivo))
    archivo.close()

leer("destino")
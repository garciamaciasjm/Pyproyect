
def fun1(a,b=2):
    print(a,b)
#Primero variables y luego keywords. sino no lo coge.
def fun2(fijo,*variable):
    print(fijo)
    print(type(variable), variable)
    for i in variable:
        print(i)

def fun2_2(*pedro):
    print(fijo)
    print(type(pedro), pedro)
    for i in pedro:
        print(i)

def sumatorio (*pedro): #metemos keywords
    suma = 0
    for i in pedro:
        suma +=i
        return i



# keywords un * tupla, 2* diccionario.

def ejer3(fijo,*variable,**pares):
    print(fijo)
    for i in variable:
        print(i)
    for i in pares:
        print(pares[i])

print("Empezamos")

fun1(1,7)
fun1(7) # Si no se le mete parámetro, asume que será b la 2, sino es la que le pongamos. por tanto todas las variables son opcionales aunque se pongan se sobeescriben por otras.


fun1(b="cadena1", a="cadena2")

fun2("fijo", "v1", "v2", "v3")  # Las mete como tupla
fun2_2("fijo2", "v1", "v2", "v3", "v4")
fun2_2(1)

sumatorio(5,6,7,8,3,4,5,6,7,8,9,)


ejer3("fijo2","v1","v2",cad1='abc',cad2=12345)

'''
operados = [5,7]
fun1(*operados) es lo mismo que :
funcion1(operados[0], operados[1])

Esto se hace para no tener que recorrer toda la tulpa, entonces metemos directamente el valor.
'''


print("Fin")

#Ejercicio:


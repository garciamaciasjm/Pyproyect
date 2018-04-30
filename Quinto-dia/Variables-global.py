
# Usar "global" es una muy mala práctica, lo mejor es que se genere otra a parte, y se devuelva por parámetro o return.
def fun1():
    global a #Cogemos la variable global a, para no generar una local.
    print(a)
    a = 7
    print(a) # Si no se pone global, da error porque se ha definido en ambito global.
a = 5
fun1()

#Se pasan parámetros por valor. -> Y no se modifican.
def fun2(a,b):
    print(a,b)
    a = a+1
    b = b+10
    print(3,a,b)

#Los tipos de datos compuestos (listas, tuplas, diccionarios.... -> mas de un valor) van por referencia y se accede a ellos de manera global.
def fun3(lista):
    lista.append(27)
    lista2 = [6,4,3]
    lista = lista2

def fun4(lista):
    lista.append(55)

a = 2
b = 3

print(1,a,b)
fun2(a,b)
print(4,a,b)

lis = [1,2,3]
print("Antes:", lis)
fun3(lis)
print("Despues", lis)
fun4(lis)
print("Despues de funcion 4:", lis)
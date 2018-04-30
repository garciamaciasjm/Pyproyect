#La función ha de estar definida antes de invocarla.
def funcion1():
    print("Empezamos funcion1")
    print("Finalizamos funcion1")

def funcion2():
    print("Empezamos funcion2")
    funcion1()
    print("Finalizamos funcion2")

def funcion3(param1):
    count = 1
    while(count <= param1):
        print(count)
        count += 1

def fun6():
    return 7,3

def ejercicio1():
    numero = int(input("Introduce el número 0:"))

    cont = 0

    while numero != 0:
        cont += 1
        numero = int(input("Introduce el número 0:"))
    print("Previamente has introducido", cont, "números mal.")

#Vamos a mostrar al usuario un menú, en el que nos indique la función que quire ejecutar, y al acabar vuelva al mismo menú:

def ejercicio1_funcion1():
    print("Este es el menú uno.")

def ejercicio1_funcion2():
    print("Este es el menú dos.")

def ejercicio1_funcion3():
    print("Este es el menú tres")

def ejercicio1_funcion4():
    print("GoodBye")
    exit()

def menu():
    print("Binvenido al menú")
    print("\n")
    print("1. Ejecutar menú uno.")
    print("2. Ejecutar menú dos.")
    print("3. Ejecutar menú tres.")
    print("4. Salir.")
    opcion = input("Seleccione una de las siguientes opciónes:")
    return opcion

def ejerMenu():
    opcion = -1
    while opcion != "0":
        opcion = menu()
        # al declararlo como entero, la comparación de los números ha de ser entre comillas
        #menu = input("Seleccione una de las siguientes opciónes:")
        # al declararlo como entero, la comparación de los números ha de ser entre comillas
        if opcion == "1":
            ejercicio1_funcion1()
        elif opcion == "2":
            ejercicio1_funcion2()
        elif opcion == "3":
            ejercicio1_funcion3()
        elif opcion == "4":
            ejercicio1_funcion4()
        else:
            print("Opción no valida")





def suma(op1,op2):
    print(op1+op2)

#una funcion que reciba dos parámetros, y que muestre los números desde el menor hasta el mayor:

def ejercicio3(numero1,numero2):

    if numero1<numero2:
        while numero1 <= numero2:
            print(numero1)
            numero1 += 1
    elif numero2<numero1:
        while numero2 <= numero1:
            print(numero2)
            numero2 += 1
    else:
        print("Los números son iguales")

#Una función a la que le metas dos numeros y imprima los que hay entre ellos y la suma de los mismos.


def ejercicio4(numero1,numero2):
    count = 0
    if numero1<numero2:
        while numero1 <= numero2:
            print(numero1)
            count = numero1 + count
            numero1 += 1
    elif numero2<numero1:
        while numero2 <= numero1:
            print(numero2)
            count = numero2 + count
            numero2 += 1
    print("El restultado total es:", count)
    #Esta función como tal no devuelve nada, por tanto para que devuelva un resultado, hacemos:
    return count

#Ejercicio en el que le metemos un número del uno al doce y nos devuelve la estación del año:

def estacion(mes):
    if mes < 3:
        return "invierno"
    elif mes <= 6:
        return "primavera"
    elif mes <= 9:
        return "verano"
    elif mes <= 12:
        return "otonio"
    else:
        return "Mes no válido"

def pruebaParametros(a,b):
    print(a,"-", b)
    a+=1
    b-=1
    print(a, "-", b)

def pruebaParametros2(a,b):
    print(a,"-", b)
    a+=1
    b-=1
    print(a, "-", b)
    return a,b

print("Empezamos")




#funcion1()
#funcion2()
#funcion1()
#ejercicio1()
#ejerMenu()
#funcion3(60)
#ejercicio3(2,60)
'''
a = ejercicio4(4,8)
# Como hemos puesto 
n1,n2 = fun6()
'''
#ejerMenu()
#menu()

#print(estacion(9))
'''
a = 5
b = 9

print("Antes:",a, "-", b)
pruebaParametros(a,b)
print("Después:",a, "-", b)


print("Antes:",a, "-", b)
a,b = pruebaParametros2(a,b)
print("Después:",a, "-", b)
'''

print("Fin")
#2.Ejerciciosba1sicos

def Menu():
    print("Bienvenido a los segundos ejercicios de Python:")
    print("\n")
    print("A:","Imprimir los números pares desde el 40 hasta el 60, ambos inclusive")
    print("B:","Imprimir los números 48, 52, 56, …, 120")
    print("C:","Calcular e imprimir la suma 1+2+3+4+5+…+50")
    print("D:","Calcular e imprimir el producto 1*2*3*4*5*…*20")
    print("E:","Calcular e imprimir la suma 50+48+46+44+…+20")
    print("F:","Programa que imprima los números impares desde el 100 hasta la unidad y calcule su suma")
    print("G:","Imprimir los números del 1 al 100 y calcular la suma de todos los números pares por un lado, y por otro, la de los impares.")
    print("H:","Introducir dos números por teclado. Imprimir los números que hay entre ellos comenzando por el más pequeno. Contar cuantos hay y cuantos de ellos son pares. Calcular la suma de los pares")
    print("I:","Imprimir y contar los números múltiplos de 3 que hay entre 1 y 100")
    print("J:","Imprimir, sumar y contar los números que son a la vez múltiplos de 2 y de 3, que hay entre la unidad y un determinado número introducido por el teclado.")
    print("K:","Introducir dos valores A y B: Si A>=B, calcular e imprimir la suma 10+14+18+…+50  Si A/B<=30, calcular e imprimir el valor de (A^2+B^2)")
    print("L:","Introducir los valores A, B y C:  Si A/B>30, calcular e imprimir A/C * B^3. Si A/B<=30, calcular e imprimir 2^2+4^2+6^2+…+30^2")
    print("\n")
    ejercicio = input("Seleccione el ejercicio que quiere visualizar:")
    print("\n")

    if ejercicio == "A":
        ejercicio2a()
    elif ejercicio == "B":
        ejercicio2b()
    elif ejercicio == "C":
        ejercicio2c()
    elif ejercicio == "D":
        ejercicio2d()
    elif ejercicio == "E":
        ejercicio2e()
    elif ejercicio == "F":
        ejercicio2f()
    elif ejercicio == "G":
        ejercicio2g()
    elif ejercicio == "H":
        ejercicio2h()
    elif ejercicio == "I":
        ejercicio2i()
    elif ejercicio == "J":
        ejercicio2j()
    elif ejercicio == "K":
        ejercicio2k()
    elif ejercicio == "L":
        ejercicio2l()
    else:
        print("La opción es incorrecta:")
        print("\n")
        Menu()



#a)Imprimir los números pares desde el 40 hasta el 60, ambos inclusive

def ejercicio2a():

    inicial = 40
    final = 60

    while inicial <= final:
        print(inicial)
        inicial += 2
    print("\n")
    fin_programa()


#b)Imprimir los números 48, 52, 56, …, 120

def ejercicio2b():

    inicial = 48
    final = 120

    while inicial <= final:
        print(inicial)
        inicial += 4
    print("\n")
    fin_programa()
#c)Calcular e imprimir la suma 1+2+3+4+5+…+50

def ejercicio2c():

    inicial = 1
    final = 50
    suma = 0

    while inicial <= final:
        print(inicial)
        suma = inicial + suma
        inicial += 1

    print("Total de la suma:",suma)
    print("\n")
    fin_programa()

#d)Calcular e imprimir el producto 1*2*3*4*5*…*20

def ejercicio2d():

    inicial = 1
    final = 20
    total = 1

    while inicial <= final:
        print(inicial)
        total = inicial * total
        inicial += 1

    print("Total de la multiplicación:", total)
    print("\n")
    fin_programa()

#e)Calcular e imprimir la suma 50+48+46+44+…+20

def ejercicio2e():

    inicial = 50
    final = 20
    suma = 0

    while inicial >= final:
        print(inicial)
        suma = inicial + suma
        inicial -= 2

    print("Total de la suma:", suma)
    print("\n")
    fin_programa()

#f)Programa que imprima los números impares desde el 100 hasta la unidad y calcule su suma

def ejercicio2f():

    inicial = 99
    final = 1
    suma = 0

    while inicial >= final:
        print(inicial)
        suma = inicial + suma
        inicial -= 2

    print("Total de la suma:", suma)
    print("\n")
    fin_programa()

#g)Imprimir los números del 1 al 100 y calcular la suma de todos los números pares por un lado, y por otro, la de los impares.

def ejercicio2g():
    inicial = 1
    final = 100
    sumapar = 0
    sumaimpar = 0

    while inicial <= final:
        print(inicial)
        if inicial % 2 == 0:
            sumapar = sumapar + inicial
        else:
            sumaimpar = sumaimpar + inicial
        inicial += 1

    print("Total de la suma de los números pares:", sumapar)
    print("Total de la suma de los números impares:", sumaimpar)
    print("\n")
    fin_programa()

#h)Introducir dos números por teclado. Imprimir los números que hay entre ellos comenzando por el más pequeno. Contar cuantos hay y cuantos de ellos son pares. Calcular la suma de los pares

def ejercicio2h():
    num1 = int(input("Introduce el primer número:"))
    num2 = int(input("Introduce el segundo número:"))

    mayor = num1
    menor = num2
    count = -1
    countpar = 0

    if num1 < num2:
        menor = num1
        mayor = num2

    while menor < mayor:
        count += 1
        menor += 1
        if ((menor % 2) == 0):
            countpar += 1

        if menor != mayor:
            print(menor)

    print("Los números entre medias son:", count)
    print("Los números pares entre medias son:", countpar)
    print("\n")
    fin_programa()

#i)Imprimir y contar los números múltiplos de 3 que hay entre 1 y 100

def ejercicio2i():

    inicial = 1
    final = 100
    suma = 0

    while inicial < 100:
        if inicial % 3 == 0:
            print(inicial)
            suma += 1
        inicial += 1
    print("La suma total de los números múltiplos de 3 es:", suma)
    print("\n")
    fin_programa()

#j)Imprimir, sumar y contar los números que son a la vez múltiplos de 2 y de 3, que hay entre la unidad y un determinado número introducido por el teclado.

def ejercicio2j():

    inicial = 1
    final = int(input("Introduce el número hasta el que quieres contar:"))
    count = 0
    suma = 0

    if final < 1:
        print("El número ha de ser positivo y mayor del número de comienzo: '1'")
        print("\n")
        ejercicio2j()

    while inicial < final :
        if (inicial % 3 == 0) and (inicial % 2 == 0):
            print(inicial)
            count += 1
            suma = inicial + suma
        inicial += 1
    print("La suma total de los números múltiplos de 2 y 3 es:", count)
    print("La suma de todos estos números es:", suma)
    print("\n")
    fin_programa()

#k)Introducir dos valores A y B: Si A>=B, calcular e imprimir la suma 10+14+18+…+50  Si A/B<=30, calcular e imprimir el valor de (A^2+B^2)

def ejercicio2k():

    A = int(input("Introduzca el primer valor:"))
    B = int(input("Introduzca el segundo valor:"))
    inicial = 10
    final = 50
    suma = 0

    if A >= B:
        while inicial <= final:
            print(inicial)
            suma = inicial + suma
            inicial += 4

        print("La suma de los números es:", suma)
    print("\n")
    if (A / B) <= 30:
        print("El resultado de (A^2+B^2) es:", (A ^ 2 + B ^ 2))
    print("\n")
    fin_programa()

#l)Introducir los valores A, B y C:  Si A/B>30, calcular e imprimir A/C * B^3 Si A/B<=30, calcular e imprimir 2^2+4^2+6^2+…+30^2bueno

def ejercicio2l():

    A = int(input("Introduzca el primer valor:"))
    B = int(input("Introduzca el segundo valor:"))
    C = int(input("Introduzca el tercer valor:"))
    inicial = 2
    final = 30
    suma = 0

    if A / B > 30:
        print("El resultado de 'A/C * B^3' es:", (A / C * (B ^ 3)))

    else:
        while inicial <= final:
            print(inicial ^ 2)
            suma = (inicial ^ 2) + suma
            inicial += 2

    print("\n")
    fin_programa()

def fin_programa():

    print("- Si desea volver al menú, pulse 'M'")
    print("- Si desea salir, pulse 'S'")
    print("\n")
    respuesta = input("Seleccione la opción:")

    if respuesta == "M":
        Menu()
    elif respuesta == "S":
        exit()
    else:
        print("La respuesta es incorrecta, seleccione de nuevo:")
        fin_programa()

print("Empieza el programa")
print("\n")
Menu()

print("Fin programa")
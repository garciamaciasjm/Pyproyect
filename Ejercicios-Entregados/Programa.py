#1.      Que pida un número del 1 al 5 y diga si es primo o no.


variable = int(input("Introduce un número del 1 al 5 y te diré si es primo o no:"))

if (variable<=0):
    print("El número introducido no es correcto")
elif (variable>5):
    print("El número introducido no es correcto")
elif ((variable / 1) == 1):
    print("El número introducido es primo")
elif ((variable / 2) == 1):
    print("El número introducido es primo")
elif ((variable / 3) == 1):
    print("El número introducido es primo")
elif ((variable / 5) == 1):
    print("El número introducido es primo")
else:
    print("El número introducido no es primo")




#2.      Que pida un número y diga si es par o impar.

numero = int(input("Introduce un número y te diré si es par o impar:"))

if ((numero%2)==0):
    print("El número introducido es par")
else:
    print("El número introducido es impar")



#3.      Que pida un número del 1 al 7 y diga el día de la semana correspondiente.

dia = int(input("Introduce un número del 1 al 7 y te diré el día de la semana:"))

if(dia < 1):
    print("El número introducido no es correcto")
elif(dia > 7):
    print("El número introducido no es correcto")
elif(dia == 1):
    print("El día de la semana es Lunes")
elif(dia == 2):
        print("El día de la semana es Martes")
elif(dia == 3):
        print("El día de la semana es Miércoles")
elif(dia == 4):
        print("El día de la semana es Jueves")
elif(dia == 5):
        print("El día de la semana es Viernes")
elif(dia == 6):
        print("El día de la semana es Sábado")
else:
        print("El día de la semana es Domingo")



#4.      Que pida un número del 1 al 12 y diga el nombre del mes correspondiente.


dia = int(input("Introduce un número del 1 al 12 y te diré el mes:"))

if(dia < 1):
    print("El número introducido no es correcto")
elif(dia >12):
    print("El número introducido no es correcto")
elif(dia == 1):
    print("El día de la semana es Enero")
elif(dia == 2):
        print("El día de la semana es Febrero")
elif(dia == 3):
        print("El día de la semana es Marzo")
elif(dia == 4):
        print("El día de la semana es Abril")
elif(dia == 5):
        print("El día de la semana es Mayo")
elif(dia == 6):
        print("El día de la semana es Junio")
elif(dia == 7):
        print("El día de la semana es Julio")
elif(dia == 8):
        print("El día de la semana es Agosto")
elif(dia == 9):
        print("El día de la semana es Septiembre")
elif(dia == 10):
        print("El día de la semana es Octubre")
elif(dia == 11):
        print("El día de la semana es Noviembre")
else:
        print("El día de la semana es Diciembre")





#5.      Que pida 3 números y los muestre en pantalla de menor a mayor.
print("Inserta 3 números y los ordenaremos de menor a mayor:")
print("\n")
numero1 = int(input("Introduce el número 1:"))
numero2 = int(input("Introduce el número 2:"))
numero3 = int(input("Introduce el número 3:"))

if((numero1 < numero2) and (numero1 < numero3)):
    if(numero2<numero3):
        print(numero1,numero2,numero3)
    else:
        print(numero1,numero3,numero2)

if((numero2 < numero1) and (numero2 < numero3)):
    if(numero1<numero3):
        print(numero2,numero1,numero3)
    else:
        print(numero2,numero3,numero1)

if((numero3 < numero1) and (numero3 < numero2)):
    if(numero1<numero2):
        print(numero3,numero1,numero2)
    else:
        print(numero3,numero2,numero1)

#6.      Que pida 3 números y los muestre en pantalla de mayor a menor.

print("Inserta 3 números y los ordenaremos de mayor a menor:")
print("\n")

numero1 = int(input("Introduce el número 1:"))
numero2 = int(input("Introduce el número 2:"))
numero3 = int(input("Introduce el número 3:"))

if((numero1 > numero2) and (numero1 > numero3)):
    if(numero2>numero3):
        print(numero1,numero2,numero3)
    else:
        print(numero1,numero3,numero2)

if((numero2 > numero1) and (numero2 > numero3)):
    if(numero1>numero3):
        print(numero2,numero1,numero3)
    else:
        print(numero2,numero3,numero1)

if((numero3 > numero1) and (numero3 > numero2)):
    if(numero1>numero2):
        print(numero3,numero1,numero2)
    else:
        print(numero3,numero2,numero1)



#7.      Que pida 3 números y los muestre en pantalla de mayor a menor en líneas distintas. En caso de haber números iguales se pintan en la misma línea.
print("Vamos a mostrar 3 números en pantalla de mayor a menor en líneas distintas. En caso de haber números iguales se pintan en la misma línea.")
numero1 = int(input("Introduce el número 1:"))
numero2 = int(input("Introduce el número 2:"))
numero3 = int(input("Introduce el número 3:"))

if (numero1 / numero2 == 1) or (numero1 / numero3 == 1) or (numero2 / numero3 == 1):

    if (numero1 == numero2 == numero3):
        print(numero1,numero2,numero3)

    elif (numero1 == numero2) and (numero2 < numero3):
        print(numero1, numero2)
        print(numero3)
    elif (numero1 == numero2) and (numero2 > numero3):
        print(numero3)
        print(numero1, numero2)

    elif (numero1 == numero3) and (numero3 < numero2):
        print(numero1, numero3)
        print(numero2)
    elif (numero1 == numero3) and (numero3 > numero2):
        print(numero2)
        print(numero1, numero3)

    elif (numero2 == numero3) and (numero3 < numero1):
        print(numero2, numero3)
        print(numero1)
    else: # (numero2 == numero3) and (numero3 > numero1):
        print(numero1)
        print(numero2, numero3)

else:
    if(numero1 < numero2) and (numero1 < numero3):
        if(numero2<numero3):
            print(numero1)
            print(numero2)
            print(numero3)
        else:
            print(numero1)
            print(numero3)
            print(numero2)

    elif(numero2 < numero1) and (numero2 < numero3):
        if(numero1<numero3):
            print(numero2)
            print(numero1)
            print(numero3)
        else:
            print(numero2)
            print(numero3)
            print(numero1)

    else: #(numero3 < numero1) and (numero3 < numero2):
        if(numero1<numero2):
            print(numero3)
            print(numero1)
            print(numero2)
        else:
            print(numero3)
            print(numero2)
            print(numero1)

#8.      Que pida un número y diga si es positivo o negativo.

numero1 = int(input("Introduce un número y te diré si es positivo o negativo:"))

if(numero1 >0):
    print("El número es positivo")
if(numero1 <0):
    print("El número es negativo")


#9.   Que sólo permita introducir los caracteres S y N.

variable1 = input("Introduce el caracter 'N' o 'S':")

if len(variable1) > 1:
    print("Error! Only 1 characters allowed!")
if((variable1 =="S") or (variable1 =="N")):
    print("El caracter es:", variable1)
else:
    print("Caracter inválido")



#10.  Que pida un número y diga si es mayor de 100.

numero1 = int(input("Introduce un número y te diré si es mayor de 100:"))

if(numero1 >100):
    print("El número es mayor de 100")
else:
    print("El número no es mayor de 100")

#11.  Que pida una letra y detecte si es una vocal.

variable1 = input("Inserte una letra en minúsculas y te diré si es vocal:")

if len(variable1) > 1:
    print("Error! Only 1 characters allowed!")

if((variable1 =="a") or (variable1 =="e")or (variable1 =="i")or (variable1 =="o")or (variable1 =="u")):
    print("La letra", variable1,"es una vocal")
else:
    print("La letra es una consonante")


#12.  Que pida tres números y detecte si se han introducido en orden creciente.

print("Introduce tres números y te diré si se han introducido de orden creciente")
numero1 = int(input("Introduce el número 1:"))
numero2 = int(input("Introduce el número 2:"))
numero3 = int(input("Introduce el número 3:"))

if(numero1 == (numero2 -1) and numero1 == (numero3 -2)):
    print("Los números se han introducido en orden creciente")
else:
    print("Los números no se han introducido en orden creciente")

#13.  Que pida tres números y detecte si se han introducido en orden decreciente.

print("Introduce tres números y te diré si se han introducido de orden decreciente")

numero1 = int(input("Introduce el número 1:"))
numero2 = int(input("Introduce el número 2:"))
numero3 = int(input("Introduce el número 3:"))

if(numero1 == (numero2 +1) and numero1 == (numero3 +2)):
    print("Los números se han introducido en orden decreciente")
else:
    print("Los números no se han introducido en orden decreciente")



#14.  Que pida 10 números y diga cuál es el mayor y cual el menor.

print("Inserta 10 números y te diré el mayor y el menor:")

n1 = int(input("Introduce el número 1:"))
n2 = int(input("Introduce el número 2:"))
n3 = int(input("Introduce el número 3:"))
n4 = int(input("Introduce el número 4:"))
n5 = int(input("Introduce el número 5:"))
n6 = int(input("Introduce el número 6:"))
n7 = int(input("Introduce el número 7:"))
n8 = int(input("Introduce el número 8:"))
n9 = int(input("Introduce el número 9:"))
n10 = int(input("Introduce el número 10:"))

if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5 and n1 > n6 and n1 > n7 and n1 > n8 and n1 > n9 and n1 > n10:
    print("El número 1 es el mayor:", n1)
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5 and n2 > n6 and n2 > n7 and n2 > n8 and n2 > n9 and n2 > n10:
    print("El número 2 es el mayor:", n2)
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5 and n3 > n6 and n3 > n7 and n3 > n8 and n3 > n9 and n3 > n10:
    print("El número 3 es el mayor:", n3)
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5 and n4 > n6 and n4 > n7 and n4 > n8 and n4 > n9 and n4 > n10:
    print("El número 4 es el mayor:", n4)
elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4 and n5 > n6 and n5 > n7 and n5 > n8 and n5 > n9 and n5 > n10:
    print("El número 5 es el mayor:", n5)
elif n6 > n1 and n6 > n2 and n6 > n3 and n6 > n5 and n6 > n4 and n6 > n7 and n6 > n8 and n6 > n9 and n6 > n10:
    print("El número 6 es el mayor:", n6)
elif n7 > n1 and n7 > n2 and n7 > n3 and n7 > n5 and n7 > n6 and n7 > n4 and n7 > n8 and n7 > n9 and n7 > n10:
    print("El número 7 es el mayor:", n7)
elif n8 > n1 and n8 > n2 and n8 > n3 and n8 > n5 and n8 > n6 and n8 > n7 and n8 > n4 and n8 > n9 and n8 > n10:
    print("El número 8 es el mayor:", n8)
elif n9 > n1 and n9 > n2 and n9 > n3 and n9 > n5 and n9 > n6 and n9 > n7 and n9 > n8 and n9 > n4 and n9 > n10:
    print("El número 9 es el mayor:", n9)
else:
    print("El número 10 es el mayor:", n10)



if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5 and n1 < n6 and n1 < n7 and n1 < n8 and n1 < n9 and n1 < n10:
    print("El número 1 es el menor:", n1)
elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5 and n2 < n6 and n2 < n7 and n2 < n8 and n2 < n9 and n2 < n10:
    print("El número 2 es el menor:", n2)
elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5 and n3 < n6 and n3 < n7 and n3 < n8 and n3 < n9 and n3 < n10:
    print("El número 3 es el menor:", n3)
elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5 and n4 < n6 and n4 < n7 and n4 < n8 and n4 < n9 and n4 < n10:
    print("El número 4 es el menor:", n4)
elif n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4 and n5 < n6 and n5 < n7 and n5 < n8 and n5 < n9 and n5 < n10:
    print("El número 5 es el menor:", n5)
elif n6 < n1 and n6 < n2 and n6 < n3 and n6 < n5 and n6 < n4 and n6 < n7 and n6 < n8 and n6 < n9 and n6 < n10:
    print("El número 6 es el menor:", n6)
elif n7 < n1 and n7 < n2 and n7 < n3 and n7 < n5 and n7 < n6 and n7 < n4 and n7 < n8 and n7 < n9 and n7 < n10:
    print("El número 7 es el menor:", n7)
elif n8 < n1 and n8 < n2 and n8 < n3 and n8 < n5 and n8 < n6 and n8 < n7 and n8 < n4 and n8 < n9 and n8 < n10:
    print("El número 8 es el menor:", n8)
elif n9 < n1 and n9 < n2 and n9 < n3 and n9 < n5 and n9 < n6 and n9 < n7 and n9 < n8 and n9 < n4 and n9 < n10:
    print("El número 9 es el menor:", n9)
else:
    print("El número 10 es el menor:", n10)




#15.  Que pida tres números e indicar si el tercero es igual a la suma del primero y el segundo.
print("Introduce tres números y te diré si el tercero es igual a la suma del primero y el segundo:")

n1 = int(input("Introduce el número 1:"))
n2 = int(input("Introduce el número 2:"))
n3 = int(input("Introduce el número 3:"))

if n3 == (n2+n1):
    print("El tercero:", n3, "es igual a la suma del primero:", n1, "y el segundo:", n2)
else:
    print("El tercero:", n3, "no es igual a la suma del primero:", n1, "y el segundo:", n2)

#16.  Que muestre un menú que contemple las opciones Archivo, Buscar y Salir, en caso de que no se introduzca una opción correcta se notificará por pantalla.
print("Mostrar un menú que contemple las opciones 'Archivo', 'Buscar' y 'Salir', en caso de que no se introduzca una opción correcta se notificará por pantalla.")
print("Menú:")
print("1. Archivo")
print("2. Buscar")
print("3. Salir")

opcion = input("Seleccione la opción numérica:")

if opcion == "1":
    print("Ha elegido la opción Archivo")
elif opcion == "2":
    print("Ha elegido la opción Buscar")
elif opcion == "3":
    print("Ha elegido la opción Salir")
else:
    print("Opción incorrecta")



#17.  Que tome dos números del 1 al 5 y diga si ambos son primos.

print("Introduce dos números del 1 al 5 y te diré si son ambos primos:")

numero1 = int(input("Inserte el primer número:"))
numero2 = int(input("Inserte el segundo número:"))

primo1 = False
primo2 = False

if (numero1<=0 or numero2<=0):
    print("No se aceptan números negativos")
elif (numero1>5 or numero2>5):
    print("no aceptamos números ,mayores de '5'")

if (numero1 / 1 == 1) or (numero1 / 2 == 1) or (numero1 / 3 == 1) or (numero1 / 5 == 1):
    primo1 = True

if (numero2 / 1 == 1) or (numero2 / 2 == 1) or (numero2 / 3 == 1) or (numero2 / 5) == 1:
    primo2 = True

if (primo1 == True) and (primo2 ==True):
    print("Ambos números son primos")
else:
    print("Ambos números no son primos")


#18.  Que tome dos números y diga si ambos son pares o impares.

print("Introduce dos números y te diré si ambos son pares o impares:")

numero1 = int(input("Inserte el primer número:"))
numero2 = int(input("Inserte el segundo número:"))

if ((numero1 % 2 ==0) and (numero2 % 2 ==0)):
    print("Ambos números son pares")
elif ((numero1 % 2 !=0) and (numero2 % 2 !=0)):
    print("Ambos números son impares")
else:
    print("Ambos números no son ni pares ni impares")


#19.  Que tome tres números y diga si la multiplicación de los dos primeros es igual al tercero.

print("Introduce tres números y te diré si la multiplicación de los dos primeros es igual al tercero")

numero1 = int(input("Inserte el primer número:"))
numero2 = int(input("Inserte el segundo número:"))
numero3 = int(input("Inserte el tercero número:"))

if (numero1*numero2 ==numero3):
    print("La multiplicación de", numero1, "x",numero2, "Es igual a:", numero3)
else:
    print("La multiplicación de", numero1, "x", numero2, "No es igual a:", numero3)




#20.  Que tome tres números y diga si el tercero es el resto de la división de los dos primeros.

print("Introduce tres números y te diré si el tercero es el resto de la división de los dos primeros")

numero1 = float(input("Inserte el primer número:"))
numero2 = float(input("Inserte el segundo número:"))
numero3 = float(input("Inserte el tercero número:"))

if (numero3 == numero1%numero2):
    print("El tercero es el resto de la división de los dos primeros")
else:
    print("el tercero no es el resto de la división de los dos primeros")


#21.  Que muestre un menú donde las opciones sean Equilátero, Isósceles y Escaleno, pida una opción y calcule el perímetro del triángulo seleccionado.

print("muestra un menú donde las opciones sean 'Equilátero', 'Isósceles' y 'Escaleno', pida una opción y calcule el perímetro del triángulo seleccionado.")

print("De los sigueintes típos de triángulo:\n")
print("1. Equilátero")
print("2. Isósceles")
print("3. Escaleno")

variable = int(input("Seleccione el número del triangulo que quiere calcular el perímetro:"))

if (variable == 1):
    equilatero = int(input("Introduzca el valor en 'cm' del lado del triángulo:"))
    print("El perímetro del triángulo es:", equilatero*3)

elif (variable == 2):
    isosceles2 = int(input("Introduzca el valor del lado repetido en 'cm':"))
    isosceles = int(input("Introduzca el valor del otro lado  en 'cm':"))
    print("El perímetro del triángulo es:", (isosceles2*2)+isosceles)

elif (variable == 3):
    escaleno1 = int(input("Introduzca el valor del primer lado en 'cm':"))
    escaleno2 = int(input("Introduzca el valor del segundo lado  en 'cm':"))
    escaleno3 = int(input("Introduzca el valor del tercer lado  en 'cm':"))
    print("El perímetro del triángulo es:", escaleno1+escaleno2+escaleno3)

else:
    print("La opción no es correcta.")

#Sirva de aclaración que el perímetro de un triángulo es siempre la suma de sus lados, pero he preferido hacerlo así para ver las tres formas diferentes de calcularlo.

#22.  Que pase de Kg a otra unidad de medida de masa, mostrar en pantalla un menú con las opciones posibles.


peso = int(input("introduzca el número de KG que quiere pasar a otra unidad:"))

print("1. Gramo")
print("2. Tonelada")
print("3. Libra")

variable = int(input("Seleccione la unidad a la que quiere pasar:"))


if (variable < 0):
    print("El valor ha de ser positivo, no existe masa negativa.")

if (variable == 1):
    print(peso, "Kg", "Son:", peso*1000, "g")

elif (variable == 2):
    print(peso, "Kg", "Son:", peso/1000, "T")

elif (variable == 3):
    print(peso, "Kg", "Son:", peso*2,20462, "libras")

else:
    print("La opción no es correcta.")



#23.  Que lea un importe bruto y calcule su importe neto, si es mayor de 15.000 se le aplicará un 16% de impuestos, en caso contrario se le aplicará un 10%.

print("Calculo de impuestos en función de si es mayor o menor de 15K")

importe = int(input("introduzca el importe bruto a calcular:"))

if (importe > 15000):
    print("El importe neto es:",importe*0.84,"€")

else:
    print("El importe neto es:",importe*0.90,"€")

#24.  Que lea una hora en hora:minutos:segundos y diga la hora que es un segundo después.

print("Introduce una hora en 24h y te diré cual será un segundo después.")

hora,minuto,segundo = int(input("introduzca la hora en formado 24h:")), int(input("introduzca el minuto:")), int(input("introduzca el segundo:"))

if (hora < 0) or ( hora > 23):
    print("La hora introducida es erronea")

elif (minuto < 0) or ( minuto > 59):
    print("El minuto introducido es erroneo")

elif (segundo < 0) or ( segundo > 59):
    print("El segundo introducido es erroneo")

else:
    print("Ha intruducido las -> ",hora,":",minuto,":",segundo)


segundo += 1

if segundo == 60:
    segundo = 0
    minuto += 1
    if minuto == 60:
        minuto = 0
        hora +=1
        if hora == 24:
            hora = 0

print("Un segundo después serán las -> ",hora,":",minuto,":",segundo)
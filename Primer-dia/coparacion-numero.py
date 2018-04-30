numero1 = int(input("Introduce el número 1:"))
numero2 = int(input("Introduce el número 2:"))
numero3 = int(input("Introduce el número 3:"))

if (numero1 > numero2 and numero1 > numero3):
    print("El número 1 es el mayor")

elif (numero2 > numero1 and numero2 > numero3):
    print("El número 2 es mayor que el número 1")

else:
    print("El número 3 es mayor")
print("Empezamos el programa")

#Tabla de multiplicar de un numero cualquiera hasta el 10 y mostrar el sumatorio de los resultados al final.
'''

numero = int(input("Introduce un número:"))

cont = 0

suma = 0

while cont <=10:
    suma = suma + cont*numero
    # suma += cont*numero
    print(numero,"x",cont,"=",numero*cont)
    cont += 1

print(suma)


#------------------------------------------------------------
'''
#contamos del uno al 100 y sumamos los impares y los sumamos mostrado el total al final.

'''
cont =1
resultado = 0

while cont <= 100:
    print(cont)
    if cont % 2 != 0:
        resultado += cont
    cont += 1
print(resultado)

#-------------------------------------------------------------

'''

#Realizamos un break

'''
cont = 0

while ( cont <= 20):
    print(cont)
    if (cont == 15):
        break
    cont = cont +1
'''

'''
cont = 0

while ( cont <= 20):
    if (cont==12):
        cont+=1
        continue #El continue vuelve al bucle de antes porque sino no continuaría el programa
    print(cont)
    if (cont == 15):
        break
    cont = cont +1

'''

#Se introducen dos números y se muestran desde el menor al mayor

'''

numero1 = int(input("Introduce un número:"))
numero2 = int(input("Introduce otro número:"))

if numero1 <= numero2:
    while (numero1 != numero2):
        print(numero1)
        numero1 += 1
else:
    while (numero2 != numero1):
        print(numero2)
        numero2 += 1

'''

#Otra manera de hacerlo:

'''

num1 = int(input("Introduce un número:"))
num2 = int(input("Introduce otro número:"))

mayor = num1
menor = num2

if (mayor<menor):
    menor = num1
    mayor = num2
while(menor<=mayor):
    print(menor)
    menor+=1
    
'''
# pedimos numeros al usuario hasta que introduzca un 0, entonces hay que mostrar el número de números que ha introducido anteriormente.

numero = int(input("Introduce el número 0:"))

cont = 0

while numero != 0:
    cont += 1
    numero = int(input("Introduce el número 0:"))
print("Previamente has introducido", cont, "números mal.")





print("Fin")
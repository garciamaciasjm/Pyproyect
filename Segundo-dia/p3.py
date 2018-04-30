print("Empezamos")

cont = 10

while ( cont <= 20):
    print(cont)
    cont = cont +1
#   cont += 1
#   cont = cont * 5
#   cont *= 5

print("-"* 25)

cont = 20
while (1<= cont):
    print(cont)
    cont -= 1


print("Fin")

print("-"*25)

cont = 5

while (cont <= 50):
    print(cont)
    cont += 5

print("-"*25)

print("-"*25)

numero = int(input("Introduce un número:"))
cont = 0

while (cont <=10):
    #print(numero,"x",cont,"=",(cont*numero))
    resultado = cont*numero
    print(resultado)
    cont += 1

print("-"*25)

cont = 1
suma = 0

while cont <=50:
    suma = suma + cont
    print(cont)
    cont += 1
print(suma)
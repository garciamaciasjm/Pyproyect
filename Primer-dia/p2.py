print("Empezamos")
'''
Estructuras de control de Flujo

- Estructuras de decisión o condicionales
IF SWITCH

- Estructuras de repeción o Bucles
WHILE DO-WHILE FOR

--> En PYTHON TENEMOS:
IF
WHILE
FOR ?

'''

#if (cond):#Cont debe devolver un boolean
#    print("Dentro del if y ejecuta lo que haya")

numero = int(input("Introduce un valor:"))

if(numero>10):
    print("El número introducido es mayor que 10")

elif(numero==10):
    print("El número introducido es igual a 10")

else:
    print("El número introducido es menor que 10")
#Siempre se debe acabar con un else !!! -> Sino hay algo que no se ha hecho bien !!


print("Fin !!!")
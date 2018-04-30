#para capturar errores
#Un programa aunque de un error tiene que terminar haciendo su funcion para la que esté diseñada.

print("Empezamos")

print("Fun1")

print(7/1)
lista = [1, 2, 3, 4, 5]

#print(7/0) # Con esto forzamos a que haya un error con el que no acaba el programa -> y SIEMPRE TIENE QUE ACABAR.


try:
    print(lista[9]) # Tampoco llegamos al final.
    fun1()
    print(7/0)
    print("Fin del try")

except ZeroDivisionError as err: # si es ZeroDivisionError le asignamos err y lo imprimimos, sino no se captura.
    print("Error 1", err)
except IndexError as err:
    print("Error 2", err)
except:
    print("Error inesperado")
finally:
    print("Esto se ejecuta siempre")





#Introduce dos numeros, y muestra la suma de los dos numeros. Si no es un numero, capturar el error y solicitar que vuelva a pedir.


error=True

while(error):
    try:
        num1= int(input("Inserta el pimer numero"))
        error = False
    except ValueError:
        print("Error de entrada")

error = True
while(error):
    try:
        num2= int(input("Inserta el segundo numero"))
        error = False
    except ValueError:
        print("Error de entrada")

print("La suma de "+str(num1)+ "+"+str(num2)+" es:", num1+num2)

print("Fin")
print("hola mundo")

a=23
b=None
#Tipos de variables que podemos usar:
print("#Tipos de variables que podemos usar:")
print(a)
print("fin")
boolean=True
entero=8
comillas=8.8
complejo=7+8j
cadena="Hola Mundo"
#Aquí empezamos a imprimir las variables.
'''
Esto 
es
el
comentario 
del
siglo
'''

print("La variable:", boolean, "Es del tipo:", type(boolean))
print(entero, type(entero))
print(comillas, type(comillas))
print(complejo, type(complejo))
print(cadena, type(cadena))


#Comenzamos con las cuentas de números:
print("#Comenzamos con las cuentas de números:")
r= 2+2
print(r)
r=2-3
print(r)
r=-8
print(r)
r=4*4
print(r)
#Dos a la sexta:
r=2**6
print(r)
r=4/5
print(r)
r=4//5
print(r)


#Concatenaciones:
print("#Concatenaciones:")
#Solo se puede concaternar del mismo tipo:

b = "dos"
nume=35
c = b + str(nume)
print(c)

#Instrucción input

#input("Pulsa intro:")

#El programa se queda esperando a que pulsamos intro.

#variable_entrada = input("Introduce el valor:")
#print(variable_entrada, type(variable_entrada))


#Booleanos

a = True
b = True
c = False
d = False

r1 = a and b
r2 = c or b
#r3 = a not True
r3 = a

print(r1)
print(r2)
print(r3)
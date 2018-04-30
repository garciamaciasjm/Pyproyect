print("Empezamos")


#STRINGS:

cadena = "Cadena de prueba"

CADENA = cadena.upper()

#Aqui no va a dar positivo, como que tiene la cadena, porque la primera C es en mayúsculas
print(CADENA.startswith("cadena"))

#Aqui si porque comparamos todo con "CADENA", que previamente lo hemos puesto en mayusculas, y luego a la variable la ponemos en mayusculas tambien.
print(CADENA.startswith("cadena".upper()))


#Usuario introduce dos numeros, y el programa verifica si son enteros, si son enteros los suma, sino ha de volver a solicitar insertar un numero al usuario.

def ejer1LeerNumeros():
    numero1 = input("Inserta el primer número")


    while not numero1.isdigit():
        numero1 = input("Error de entrada, inserta el primer número")

    numero2 = input("Error de entrada, inserta el segundo número")

    while not numero2.isdigit():
        numero2 = input("Inserta el segundo número")

    print("La suma es", int(numero1)+int(numero2))

def ejemOrdChr():
    variable1 = 65
    print(chr(variable1))
    variable2 = "b"
    print(ord(variable2))

def ejerMayus():

    texto1 = input("Inserta letras en mayusculas")

    for i in texto1:
        if (ord(i) > ord("Z") or ord(i) < ord("A")):
            return False
    return True

def ejerMayus1():

    texto1 = input("Inserta letras en mayusculas")

    for i in texto1:
        if (ord(i) <= ord("z") and ord(i) >= ord("a")):
            return False
    return True

#funcion que le pases una cadena y te la pase a mayusculas:

def toMayus():
    variable1 = input("Inserta una cadena")
    resultado = ""

    for i in variable1:
        if (ord(i) <= ord("z")) and (ord(i) >= ord("a")):
            resultado = resultado + i.upper()
        else:
            resultado = resultado + i

def toMayus1(cadena):

    nuevacadena = ""
    dif = ord("a") - ord("A")

    for i in cadena:
        if (ord(i) <= ord("z")) and (ord(i) >= ord("a")):
            nuevacadena = nuevacadena+chr(ord(i)-dif)
        else:
            nuevacadena = nuevacadena+i
    return nuevacadena

#ejer1LeerNumeros()

#ejemOrdChr()

#print(ejerMayus())

#print(toMayus1("dsfghjkllkjhgf"))

print("Fin")



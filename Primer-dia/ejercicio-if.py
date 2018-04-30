edad = int(input("Introduce la edad del colega:"))

if (edad < 18):
    print("El colega es menor de edad")
elif (18 <= edad < 65):
#elif (18<=edad and num<65)
    print("El colega es una persona adulta")
else:
    print("El colega es un anciano")
nota = float(input("Introduce la nota obtenida:"))

if (nota < 5):
    print("Ha suspendido")
elif(nota == 10):
    print("Ha obtenido matrícula de honor")
elif (nota > 9):
    print("Ha obtenido sobresaliente")
elif (nota > 7):
    print("Ha obtenido notable")
elif (nota >= 6):
    print("Ha obtenido bien.")
else:
    print("Ha aprobbado la asignatura")
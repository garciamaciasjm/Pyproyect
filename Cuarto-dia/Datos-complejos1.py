import random

print("Empezamos")
#Matriz: lista de listas
mat = [[1,2],[3,4],[5,6]]

#print(mat)
def mostrar(mat):
    for i in mat:
        for j in i:
            print(j, end="\t") # las dobles comillas hace que no haya salto de línea entre cada impresion.
        print()

#mostrar(mat)

#crea una matriz con 10 posiciones,en la que metas los numeros del 1 al 10 en la primera, del 20 al 29 en la segunda.... e imprimirlos.


def mat10():
    mat = []
    lista = []
    for i in range(1,101):
        lista.append(i)
        if (i %10 == 0):
            mat.append(lista)
            lista = []

    mostrar(mat)


#mat10()


def generarTablero():
    tab = [["0","0","0","0","0","0","0","0","8","0",], ["0","0","0","0","0","0","0","0","8","0",], ["0","0","0","4","0","0","0","0","8","0",], ["0","0","0","4","0","0","0","0","8","0",], ["0","0","0","4","0","0","0","0","0","0",], ["0","0","0","4","0","0","0","0","0","0",], ["0","0","5","5","5","5","5","0","0","0",], ["0","0","0","0","9","9","9","9","9","0",], ["0","0","0","0","0","0","0","0","0","0",], ["0","0","0","0","0","0","0","0","0","0",]]
    return tab

def jugar(tab):
    tocado = False
    while (not (tocado)):
        y = random.randint(0, len(tab)- 1)
        x = random.randint(0, len(tab[y])- 1)
        if (tab[y][x] == "0" or tab[y][x] == "X"):
            tab[y][x] ="X"
        else:
            tab[y][x] = "T"
            tocado = True


def juegoBarcos():
    tab = generarTablero()
    mostrar(tab)
    print("---------")
    jugar(tab)
    mostrar(tab)


juegoBarcos()
print("Fin")
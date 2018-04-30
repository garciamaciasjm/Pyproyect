import random

def mostrar(mat):
    for i in mat:
        for j in i:
            print(j, end="\t") # las dobles comillas hace que no haya salto de línea entre cada impresion.
        print()

def generarTablero():
    tab = [["0","0","0","0","0","0","0","0","8","0"], ["0","0","0","0","0","0","0","0","8","0"], ["0","0","0","4","0","0","0","0","8","0"], ["0","0","0","4","0","0","0","0","8","0"], ["0","0","0","4","0","0","0","0","0","0"], ["0","0","0","4","0","0","0","0","0","0"], ["0","0","5","5","5","5","5","0","0","0"], ["0","0","0","0","9","9","9","9","9","0"], ["0","0","0","0","0","0","0","0","0","0"], ["0","0","0","0","0","0","0","0","0","0"]]
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
            #input("El barco a sido tocado")
            #mostrar(tab)
            #return tab


def juegoBarcos():
    tab = generarTablero()
    mostrar(tab)
    print("---------")
    jugar(tab)
    mostrar(tab)

def finaliza(mat):
    for i in tab:
        for j in i:
            while j.isdigit():
                jugar(tab)





print("Empezamos")
juegoBarcos()
# for i in tab:
#     for j in i:
#         while j.isdigit():
#             jugar(tab)


print("Fin")
a = True
b = True
c = False
d = False

r1 = a and b
r2 = c or b
#Le cambiamos el valor
r3 = not a

print(r1)
print(r2)
print(r3)


#------------------
print("-"*25)

a = (5==6)
print(a)

a = 3<4
print(a)

numHijos=5
renta = 20000
nota = 7
beca = numHijos>=3 and renta<=15000 and nota>=5
print("concedida:", beca)
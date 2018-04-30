#Vamos a trabajar con bases de datos relacionales (SQL)
#Filas = Registros = Tuplas
#Columnas = Atributos = Campos -> Siempre hay uno especial, que es la clave o la primary key
#Foreing Key -> es el campo que sirve para relacionar una base de datos con otra primary key de otra tabla. Si no se pone no se relacionan entre si.

import sqlite3


conn = sqlite3.connect('Concesionario.sqlite')

c = conn.cursor()


comando1 = "INSERT INTO clientes VALUES (NULL, '47215859K', 'jose', 'dacio', '61785478965')"
c.execute(comando1)
conn.commit()
#comando2 = "INSERT INTO clientes VALUES (NULL, 'dni2', 'nom2', 'dir2', 'tel2')"
'''

cont = 1
while cont <= 2:
    comandoSql ="INSERT INTO clientes VALUES (NULL"+str(cont)+", 'dni', 'nom1', 'dir1', 'tel1')"
    c.execute(comandoSql)
    cont2 = 1
    while cont2 <= 2:
        comandoSql2 = "INSERT INTO clientes VALUES (NULL, 'dni1', 'nom1', 'dir1', 'tel1')"
        c.execute(comandoSql2)
        cont2 = cont2 + 1
    cont = cont + 1

conn.commit() # para guardar

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

# 
conn.close()
'''
print("***********************************")

c.execute("SELECT * FROM clientes")
registros = c.fetchall()#devuelve todos los valores y recorro toda la lista.
print(type(registros))
for registro in registros:
    print(registro, type(registro))

print("--------------------")

c.execute("SELECT * FROM vehiculos")
registro = c.fetchone() # devuelve de uno en uno.
while registro!=None:
    print(registro)
    registro = c.fetchone()

c.close()
conn.close()

import sqlite3

connection = sqlite3.connect('database.db')

#-------------------------------------------------
#-Cursor------------------------------------------
#-------------------------------------------------
#Para ejecutar sentencias de SQLite en Python, 
#se necesita un objeto cursor.
#Ahora podemos usar el objeto cursor para llamar al método execute (),
#el cual sirve para ejecutar cualquier consulta SQL.
#-------------------------------------------------

#crear tabla
def sql_table(connection):
    cursor = connection.cursor() #crea un objeto cursor utilizando el objeto de conexión
    cursor.execute("CREATE TABLE IF NOT EXISTS datos (worker_id integer PRIMARY KEY, name text)")
    connection.commit() # guardar todos los cambios que hacemos

#insertar dato
def sql_insertdata(connection):

    cursor = connection.cursor()
    cursor.execute("INSERT INTO datos VALUES(1, 'John')")
    connection.commit() 


def sql_fetch(connection):

    cursor = connection.cursor()
    cursor.execute('SELECT password, id FROM users') #obtener todos los datos de una tabla de una base de datos
    rows = cursor.fetchall()#almacenamos los valores en una variable/ lista

    for row in rows: # recorreremos la variable e imprimiremos todos los valores.

        print(row)
    cursor.execute('SELECT  id, username FROM users') #obtener todos los datos de una tabla de una base de datos
    rows = cursor.fetchall()#almacenamos los valores en una variable/ lista

    for row in rows: # recorreremos la variable e imprimiremos todos los valores.

        print(row)
    cursor.execute('SELECT password, username FROM users') #obtener todos los datos de una tabla de una base de datos
    rows = cursor.fetchall()#almacenamos los valores en una variable/ lista

    for row in rows: # recorreremos la variable e imprimiremos todos los valores.

        print(row)

sql_fetch(connection)
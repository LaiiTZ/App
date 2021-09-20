import time
import sqlite3
from sqlite3 import Error

class SensorBase(object):

	def __init__(self,topico,valor):
		self.topico = topico;
		self.valor = valor;

	def mostrar(self):
    		print(self.valor)     

	def guardar(self):
		connection = sqlite3.connect('datos.db') # crea base de datos aa
		cursor = connection.cursor() #crea un objeto cursor utilizando el objeto de conexión
		cursor.execute("CREATE TABLE IF NOT EXISTS mqtt (id integer PRIMARY KEY, fecha datetime, topico varchar, name varchar)") # creamos la tabla (si no existe)
		add_registro = ("INSERT INTO mqtt (`fecha`, `topico`, `valor`) VALUES (now(), %s, %s)")
		#la funcion "now()" de la libreria "time" es utilizada para mostrar la fecha y hora actual
		# la funcion "%s" se usa para tomar dos variables desde el exterior
		data_registro = (self.topico,self.valor) # guardamos las dos variables que luego seran agregadas a la funcion INSERT
		cursor.execute(add_registro, data_registro) # se suma la funcion INSERT
		connection.commit() # guardar todos los cambios que hacemos
		connection.close() # despues de usar la base de datos, cerramos la conexion, ya que es considerada una buena practica
		
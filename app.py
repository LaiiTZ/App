from flask import Flask, render_template, request, redirect, flash, session, escape, make_response
from flask_sqlalchemy import SQLAlchemy #--> libreria de base de datos
from werkzeug.security import generate_password_hash, check_password_hash #--> libreria para cifrar contrasenias
import sqlite3

import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db" # "os.path.abspath(os.getcwd())" genera ruta de trabajo actual

app = Flask(__name__)
app.jinja_env.trim_blocks = True # para que el html se vea bien identado
app.secret_key = 'xzZ7W9LtLQk$hMbP'
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir # ruta de la base de datos
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app) #--> Creacion de la base de datos en programa

class Users(db.Model): # esquema de base de datos con clase de python
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
print("------------------------------\n------------------------------\n---Dev By: LtZ & Vikinguito---\n------------------------------\n------------------------------")
@app.route("/") # index/home
def index():
  if "username" in session: # detectar si el usuario esta logueado
    flash("%s"% escape (session["username"]), "username") # mostrar el nombre del usuario en la pagina con la clase username
    return render_template("indexl.html")
  else:
    return render_template("index.html")

@app.route("/signup/", methods=["GET", "POST"] ) # seccion de logueo
def signup():
  if "username" in session:
    return redirect("/")
  else:
    if request.method == "POST": # si el metodo que recibimos es de tipo post
        user = Users.query.filter_by(username=request.form["username"]).first()
        if user: # consultamos si hay un usuario con esa cuenta
          flash("Ese usuario ya existe, intenta con otro", "error") # mostramos un mensaje tipo flash con una clase asignada para luego poder ponerle color con css
        else:
          if request.form["password"] == request.form["password2"]:
            hashed_pw = generate_password_hash(request.form["password"], method="sha256") # recibe la contrasenia que ingreso el usuario y la cifra usando la libreria "werkzeug.security"
            new_user = Users(username=request.form["username"], password=hashed_pw) # creamos el usuario
            db.session.add(new_user)
            db.session.commit()
            flash("Registrado correctamente, inicia sesion para ingresar!", "success")
            return redirect("/login/") #redireccionamiento hacia a la pagina de logueo
          else:
            flash("Las contraseñas deben ser iguales.", "error")
    return render_template("signup.html")


@app.route("/login/", methods=["GET", "POST"])
def login():
  if "username" in session:
    return redirect("/")
  else:
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form["username"]).first() # busca en los usuarios en la database y elige el primero
        if user:
          if check_password_hash(user.password, request.form["password"]): # si el nombre de usuario existe, coompara las contrasenias con check_password_hash
            session["username"] = user.username
            return redirect("/")
          else:
            flash("Contraseña incorrecta.", "error")
        else:
          flash("El usuario ingresado no existe.", "error")
    return render_template("login.html")

@app.route("/logout")
def logout():
  session.pop("username", None) #session.pop(username) sirve para desloguear, el none es para que no haya errores si no encuentra la cookie que queremos borrar
  return redirect("/")
 
@app.route("/quienes-somos/") # secciones a las que todos los usuarios pueden entrar
def quienessomos():
  return render_template("quienes-somos.html")

@app.route("/FAQ/")
def FAQ():
  return render_template("faq.html")
  
@app.route("/registro/") # secciones a las que solo se puede acceder si estas logueado
def registro():
  return render_template("registro.html")

@app.route("/client/")
def client():
  if "username" in session: # detectar si el usuario esta logueado
  # mostrar el nombre del usuario en la pagina
    return "wea en mantenimiento, no andi weando por aqui, no vei que no entra? anda pa otro lao hermano %s"% escape (session["username"])#render_template("indexl.html")
  else:
    resp = make_response(redirect("/login/"))
    resp.set_cookie("client-red", "nologged")
    flash("Debes inciar sesion para acceder a esta zona.", "error")
    return resp

@app.route("/about-us/") # 
def aboutus():
  if "username" in session: # detectar si el usuario esta logueado
    flash("%s"% escape (session["username"]), "username") # mostrar el nombre del usuario en la pagina con la clase username
    return render_template ("aboutusl.html")
  else:
    return render_template ("aboutus.html")

@app.route("/test2/", methods=["GET", "POST"])
def test():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT password, username FROM users')
    rows = cursor.fetchall()#almacenamos los valores en una variable/ lista

    for row in rows: # recorreremos la variable e imprimiremos todos los valores.
     print(row)
     flash((row), "username")
    #//////////////////////////////////////////////////////////////////////////////////
    cursor.execute('SELECT password FROM users')
    rows = cursor.fetchall()#almacenamos los valores en una variable/ lista

    for row in rows: # recorreremos la variable e imprimiremos todos los valores.
     print(row)
     flash((row), "password")
    return render_template ("test.html")

if __name__ == "__main__":
  db.create_all() # crear la base de datos(SI NO ESTA CREADA)
  app.run(debug=True)
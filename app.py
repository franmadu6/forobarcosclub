import functools
from requests_html import HTMLSession
from bs4 import *
from tabulate import tabulate
from flask import Flask, redirect, render_template, request, session, url_for,abort
import os
from opgg import *

app = Flask(__name__, template_folder="templates")

#---------pg de inicio
@app.route('/',methods=["GET"])
def inicio():
    listaj=obtener_jugador()
    return render_template("index.html",error= None,listaj=listaj)

#-----------pg premios
@app.route('/estadisticas',methods=["GET","POST"])
def obusuario():
        
    return render_template('estadisticas.html',error= None)

#activar estas lineas para que vaya en heroku.
if __name__ == '__main__':
    port=os.environ["PORT"]
app.run('0.0.0.0',int(port), debug=True)

#activar esta linea para que vaya en la termial.
#app.run(debug=True)

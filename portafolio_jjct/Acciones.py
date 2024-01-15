
from flask import Flask
from flask import flash
from flask import request
from flask import render_template
from flask import redirect

from database import Database
from database import engine
from database import db_session
from flask import url_for

import models

app = Flask(__name__)
    
Database.metadata.create_all(engine)

@app.get('/')  
def home():  
    almacen = db_session.query(models.almacen).all()
    return render_template("home.html", almacen=almacen)


@app.post('/insertar')
def insertar():
    marca = request.form['marca']
    modelo = request.form['modelo']
    piezas = request.form['piezas']
    
    nuevo_almacen = models.almacen(
        marca = marca,
        modelo = modelo,
        piezas = piezas,
    )
    db_session.add(nuevo_almacen)
    db_session.commit()
    return redirect("/")

@app.get('/eliminar/<id>')
def eliminar(id):
   almacen = db_session.query(models.almacen).get(id)
   
   if almacen == None:
       flash('ID no encontrado')
       return render_template('home.html')
   
   db_session.delete(almacen)
   db_session.commit()
   
   return redirect(url_for('home'))  
   
@app.post('/actualizar/<id>')
def actualizar(id):
    almacen = db_session.query(models.almacen).get(id)
       
    if almacen == None:
        flash('ID no encontrado')
        return redirect (url_for('home'))
       
    marca = request.form['marca']
    modelo = request.form['modelo']
    piezas = request.form['piezas']
       
    if almacen == None:
        flash('No hay nada')
        return redirect (url_for('home'))
       
    almacen.modelo = modelo
    almacen.marca = marca
    almacen.piezas = piezas
       
    db_session.add(almacen)
    db_session.commit()
       
    return redirect(url_for('home'))
   
   
   
if __name__ == '__main__':
    app.run('0.0.0.0', 6969, debug=True)
    

    
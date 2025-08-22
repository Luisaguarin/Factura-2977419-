from flask import Flask, render_template
from app import app

@app.route("/")
def index():
    return render_template('index.html' , title= "App facturacion")

@app.route("/clientes")
def clientes():
    return render_template('clientes.html' , title="Lista de clientes")

@app.route ("/from_cliente")
def form_cliente():
    return render_template('from_cliente.html' , title="Formulario de clientes")

    
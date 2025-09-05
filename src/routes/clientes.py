# src/clientes.py
from flask import Blueprint, render_template, request, redirect, url_for

clientes_bp = Blueprint('clientes', __name__) 

@clientes_bp.route('/clientes')
def clientes():
    return render_template('clientes.html')

@clientes_bp.route('/agregar_cliente', methods=['POST'])
def agregar_cliente():
    return redirect(url_for('clientes.clientes'))  # Nota: clientes.clientes

@clientes_bp.route('/editar', methods=['POST'])
def editar():
    return render_template('editar.html')

@clientes_bp.route('/submit', methods=['POST'])
def submit():
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    mensaje = request.form['mensaje']
    return f'Formulario enviado! Nombre: {nombre}, Email: {email}, Teléfono: {telefono}, Mensaje: {mensaje}'



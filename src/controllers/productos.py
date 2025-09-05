from flask import Blueprint, render_template, redirect, url_for

productos_bp = Blueprint('productos', __name__, url_prefix='/productos')


@productos_bp.route('/')
def vista_principal_productos():
    return render_template('productos.html')


@productos_bp.route('/formulario_producto')
def formulario_producto():
    return render_template('formulario_producto.html')


@productos_bp.route('/lista_productos')
def lista_productos():
    return render_template('lista_productos.html')


@productos_bp.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    return redirect(url_for('productos.lista_productos'))  


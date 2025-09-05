from flask import render_template, request
from flask_controller import FlaskController
from src.models.productos import Productos
from src.models.categorias import Categorias
from src.app import app
from flask import Blueprint, render_template

productos_bp = Blueprint('productos', __name__, url_prefix='/productos')

@productos_bp.route('/')
def listar():
    return 'Listado de productos'


@app.route('/productos')
def productos():
    productos_list = Productos.traer_todos()  
    return render_template('productos.html', productos=productos_list, titulo='Listado de Productos')



@app.route('/producto/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        descripcion = request.form.get('descripcion')
        cantidad_inventario = request.form.get('cantidad_inventario')
        precio_unitario = request.form.get('precio_unitario')
        unidad_medida = request.form.get('unidad_medida')
        categoria = request.form.get('categoria')

        producto = Productos(
            codigo,
            descripcion,
            float(precio_unitario),
            unidad_medida,
            float(cantidad_inventario),
            int(categoria)
        )
        producto.crear_producto()

    
    categorias = Categorias.traer_categorias()
    return render_template('formulario_producto.html', titulo='Crear producto', categorias=categorias)

@app.route('/productos/nuevo')
def nuevo_producto():
    return render_template('productos/formulario_producto.html')

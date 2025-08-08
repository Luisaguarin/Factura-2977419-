from flask import Flask, render_template, request
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
import sqlite3
import os
import pymysql


app = Flask(__name__)

    
engine = create_engine("mysql+pymysql://root:@localhost/factura_243")
conection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
Base.metadata.bind = engine

@app.route('/conexion')
def conexion():
    return "Conexión exitosa a la base de datos"


# Conexión a la base de datos de productos
def get_db_connection():
    conn = sqlite3.connect(os.path.join('database', 'productos.db'))
    conn.row_factory = sqlite3.Row
    return conn

# Conexión a la base de datos de clientes
def get_clientes_connection():
    conn = sqlite3.connect(os.path.join('database', 'clientes.db'))
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes')
def clientes():
    conn = get_clientes_connection()
    clientes = conn.execute('SELECT * FROM clientes').fetchall()
    conn.close()
    return render_template('clientes.html', clientes=clientes)

@app.route('/productos')
def productos():
    conn = get_db_connection()
    productos = conn.execute('SELECT * FROM productos').fetchall()
    conn.close()
    return render_template('productos.html', productos=productos)

@app.route('/formulario_producto', methods=['GET', 'POST'])
def formulario_productos():
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        descripcion = request.form.get('descripcion')
        cantidad_inventario = request.form.get('cantidad_inventario')
        precio_unitario = request.form.get('precio_unitario')
        unidad_medida = request.form.get('unidad_medida')
        categoria = request.form.get('categoria')
        producto = Productos(codigo, descripcion, float(precio_unitario), unidad_medida, float(cantidad_inventario), int(categoria))
        producto.crear_producto()
        print("Entro por POST")
        print(codigo)
    return render_template('formulario_producto.html', titulo='crear un producto')




@app.route('/facturar')
def facturar():
       return "pagina de facurar (en construccion)"
   
@app.route('/producto/nuevo')
def nuevo_producto():
    return render_template('formulario_producto.html', titulo='crear producto')
   
@app.route('/se_guardo')
def se_guardo():
       return render_template('se_guardo.html', titulo='Guardado')
    
class Productos(Base):
    __tablename__ = 'productos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(300), unique=True, nullable=False)
    valor_unitario = Column(Float(10, 8))
    unidad_medida = Column(String(3), unique=True, nullable=False)
    cantidad_stock = Column(Float(10, 8))
    categoria = Column(Integer, nullable=False)

    def __init__(self, codigo, descripcion, valor_unitario, unidad_medida, cantidad_stock, categoria):
        self.codigo = codigo
        self.descripcion = descripcion
        self.valor_unitario = valor_unitario
        self.unidad_medida = unidad_medida
        self.cantidad_stock = cantidad_stock
        self.categoria = categoria

    def crear_producto(self):
        Session.add(self)
        Session.commit()



    
class Categorias(Base):
    __tablename__="Categorias"
    id = Column(Integer, primary_key=True)
    nombre_categoria = Column(String(300), unique=True, nullable=False)

Base.metadata.create_all(engine)

   
   
if __name__ == '__main__':
    app.run(debug=True)






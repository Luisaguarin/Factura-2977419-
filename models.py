from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, column, Integer, String, Float, Foreignkey
from sqlalchemy.orn import declarative_base, sessionnaker 
import pymysql

engine = create_engine("mysql+pymysql://root:@localhost/repositorio") 
conection = engine.connect()

Base = declarative_base()
Base.netadata.bind = engine

session = sessionmaker(bind=engine)
  
class producto(Base):
    _tablename_ = "productos"
    id = db.Column(db.Intreger , primary_key=True)
    descripcion = db.Column(db.String(200), unique=True, nullable=False)
    unidad_medida = db.Column(db.String(4), unique=True, nullable=False)
    cantidad_stock = db.Column(db.Integer, unique=True, nullable=False)
    valor_unitario = column(float(10,8))
    precio = db.Column(db.Integer, unique=True, nullable=False)
    categoria = Column(Integer, Fore1gnkey('categorias.id'),nullable=False)
    
    def _init_(self,descripcion,unidad_medida,cantidad_stock,valor_untario,precio,categoria):
        self.descripcion = descripcion
        self.unidad_medida = unidad_medida
        self.cantidad_stock =cantidad_stock
        self.valor_unitario = valor_unitario
        self.precio = precio
        self.categoria =categoria
        
    def agregar_producto():
        session = session()
        producto = session.add(producto)
        session.comit()
        return producto
    
class categorias(Base):
    _tablename_ = "categorias"
    id = Column (Integer, primary_key=True)
    categoria = Column(Sring(100),unique=True,nullable=False)
    
class Clientes(Base):    
    id = db.Column(db.Intreger , primary_key=True)
    nombre = db.Column(db.String(200), unique=True, nullable=False)
    tipo_identificacion = db.Column(db.String(28), unique=True, nullable=False)
    numero_identificacion = db.Column(db.String(28), unique=True, nullable=False)
    direccion = db.Column(db.String(200), unique=True, nullable=False)
    telefono = db.Column(db.String(28), unique=True, nullable=False)
    
class vendedores(Base):
    
    id = db.Column(db.Intreger , primary_key=True)
    nombre = db.Column(db.String(200), unique=True, nullable=False)
    tipo_identificacion = db.Column(db.String(28), unique=True, nullable=False)
    numero_identificacion = db.Column(db.String(28), unique=True, nullable=False)
    telefono = db.Column(db.String(28), unique=True, nullable=False)
    

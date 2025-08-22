from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from src.models import session, Base
from src.models.categorias import Categorias
from sqlalchemy.orm import declarative_base


Base = declarative_base()

engine = create_engine('sqlite:///mydatabase.db')

class Productos(Base):

    __tablename__ = 'productos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(50), nullable=False, unique=True)
    descripcion = Column(String(300), nullable=False)
    valor_unitario = Column(Float(10, 2))
    unidad_medida = Column(String(3), nullable=False)
    cantidad_stock = Column(Float(10, 2))
    categoria = Column(Integer, nullable=False)
    
    
    def __init__(self, codigo, descripcion, valor_unitario, unidad_medida, cantidad_stock, categoria):
        self.codigo = codigo
        self.descripcion = descripcion
        self.valor_unitario = valor_unitario
        self.unidad_medida = unidad_medida
        self.cantidad_stock = cantidad_stock
        self.categoria = categoria
    
    @classmethod
    def traer_todos(cls):
        # tu lógica aquí
        pass

    def crear_producto(self):
        Session.add(self)
        Session.commit()
        
    Base.metadata.create_all(engine)
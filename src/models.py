class Cliente(db.Model):
    
    __tablename__ = 'clientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    documento = db.Column(db.String(100), nullable=False)
    
class Productos(Base):

    __tablename__ = 'productos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(50), nullable=False, unique=True)
    descripcion = Column(String(300), nullable=False)
    valor_unitario = Column(Float(10, 2))
    unidad_medida = Column(String(3), nullable=False)
    cantidad_stock = Column(Float(10, 2))
    categoria = Column(Integer, nullable=False)
    
    
    def __init__(self):
        print ('cliente listo')
    
from sqlalchemy import Column, Integer, String
from src.models import session, Base
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Categorias(Base):
    __tablename__ = "Categorias"

    id = Column(Integer, primary_key=True)
    nombre_categoria = Column(String(300), unique=True, nullable=False)

    def __init__(self, nombre_categoria):
        self.nombre_categoria = nombre_categoria

    @classmethod
    def traer_categorias(cls):
        return session.query(cls).all()

    @classmethod
    def obtener_categoria_por_id(cls, id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def actualizar_categoria(cls, id, nuevo_nombre):
        categoria = session.query(cls).filter_by(id=id).first()
        if categoria:
            categoria.nombre_categoria = nuevo_nombre
            session.commit()

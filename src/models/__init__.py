from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import sqlite3
import os
import pymysql

engine = create_engine("mysql+pymysql://root:@localhost/factura_243")

conection = engine.connect()

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()
Base.metadata.bind = engine


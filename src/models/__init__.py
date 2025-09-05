from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import sqlite3
import os
import pymysql
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base = declarative_base()
engine = create_engine("mysql+pymysql://root:@localhost/factura_243")

conection = engine.connect()

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()
Base.metadata.bind = engine


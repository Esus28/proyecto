from database import Database
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date

class almacen(Database):
    __tablename__ = 'almacen'
    id = Column(Integer, primary_key=True)
    marca = Column(String(20))
    modelo = Column(String(30))
    piezas = Column(String(10))
    

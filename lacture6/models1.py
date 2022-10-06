#This model become libary for aap.py


from ast import Str
from enum import Flag
from tkinter import Text
from xmlrpc.client import Boolean
from sqlalchemy import Column,Integer, String , DateTime,PickleType
from sqlalchemy.ext.declarative import declarative_base




Base = declarative_base()

class Member(Base):
    __table__ = 'member'
    id = Column(Integer,primary_key = True , nullable = False)
    name = Column(String(100), nullable = False)
    description = Column(Text,nullable = True)
    join_date  = Column(DateTime, nullable = False)
    vip  = Column(Boolean , nullable = False)
    number = Column(float , nullable = False)


    def __repr__(self) :
        return "<UserModel model {}>".format(self.id)


        
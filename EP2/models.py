from ast import Str
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key = True)
    name  = Column(String)
    fullname = Column(String)
    nickname = Column(String)


    def __repr__(self):
        return "<User(name ='%s',fullname = '%s',nikcname = '%s')>"%(
            self.name , self.fullname , self.nickname)


            

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,INTEGER,String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship,backref
import uuid 

engine = sqlalchemy.create_engine('sqlite:///po.db')
Base = declarative_base()

class Order_Product(Base):
    __tablename__ = 'order_product'
    id = Column(String(35),primary_key = True ,unique = True)
    order_id = Column(INTEGER,ForeignKey('orders.id'),primary_key = True)
    product_id = Column(INTEGER,ForeignKey('products.id'),primary_key = True)
    quantity = Column(INTEGER)


    order = relationship("Order" , backref(
        'order_products', cascade = "all, delete-orphan"))
    product = relationship("Product",backref =backref(
        'order_products' , cascade = 'all, delete-orphan'))


    def __init__(self, order = None , product = None , quantity = None):
        self.id = uuid.uuid4().hex
        self.order = order 
        self.product = product
        self.quantity = quantity

    def __repr__(self):
        return '<Order_Product {}>'.format(self.order.name +" "+self.product.name)

class Product(Base):
    __tablename__  = 'products'
    id = Column(String(35),primary_key = True , unique = True)
    name =  Column(String(80) , nullable = False)



    def __init__(self,name):
        self.id = uuid.uuid4().hex
        self.name = name 
        self.orders  = []

    def __repr__(self):
        return "<Product {}>".format(self.name)

class Order(Base):
    __talble__ = 'orders'
    id = Column(String(35) , primary_key = True , unique = True)
    name = Column(String(80), nullable = False)


    product = relationship(
        "Product",secondary = 'order_product',viweonly = True)


    def add_products(self , items):
        for product , qty , in items:
            self.order_products.app
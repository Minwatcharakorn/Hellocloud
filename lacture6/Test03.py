import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models  import Base,User



engine = create_engine("sqlite:///user.db",echo = False)


Session = sessionmaker(bind=engine)
session = Session()


for  instance in session.query(User).order_by(User.id):
    print(instance.name , instance.fullname)
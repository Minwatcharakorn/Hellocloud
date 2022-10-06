#Last Example between Test 1 to Test4 

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models  import Base,User



engine = create_engine("sqlite:///user.db",echo = False)


Session = sessionmaker(bind=engine)
session = Session()



for instance in session.query(User).filter(User.name.in_(('user1','user2'))):
    print(instance.name , instance.fullname)


    
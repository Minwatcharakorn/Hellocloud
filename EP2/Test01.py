import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models  import Base,User



engine = create_engine("sqlite:///user.db",echo = False)


#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name = 'user1', fullname = 'Ed Jones',nickname = 'Ed')
user2 = User(name = 'user2', fullname = 'Ed Jones',nickname = 'Ted')
user3 = User(name = 'user3', fullname = 'STEd Jones',nickname = 'STed')
user4 = User(name = 'user4', fullname = 'WTEd Jones',nickname = 'WTed')


session.add_all([user1,user2,user3,user4])
session.commit()

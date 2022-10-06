#This file we will be using model01 since the name will duplicate with models . 
from models1 import Base , Member
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

#Create engine 

db_uri = 'sqlite///Ex.db'
engine =create_engine(db_uri,echo = False)



#Create all table
#Base.metdata.drop_all(engine)
Base.metadata.create_all(engine)



Session =sessionmaker(bind = engine)
session = Session()


user = Member(
    name = 'toddy',
    description = 'im testing this',
    vip = True,
    join_date = datetime.date.today(),
    number = 45.0

)


session.add(user)
session.commit()
print(user)
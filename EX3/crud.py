## crud.py #

from datetime import datetime
from contextlib import contextmanager
from sqlalchemy.orm  import sessionmaker
from sqlalchemy import create_engine
import yaml 

#เติมข้อมูลให้ครบก่อนใน configs.py !!!!#
from configs    import DATEBASE_URI , f_yam
from models2  import Base , Book

engine = create_engine(DATEBASE_URI)

Session = sessionmaker(bind = engine)


@contextmanager
def session_scope():
    session = Session()
    try: 
        yield session
        session.commit()
    except Exception:
        session.rollback()
        print('Error')
        raise
    finally:
        session.close()


def recreate_database():
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def load_yaml(fn):
    with session_scope() as s:
        for data in yaml.load_all(open(fn), Loader=yaml.FullLoader):
                bookyml = Book(**data)
                s.add(bookyml)



if __name__ == '__main__':
    recreate_database()
    #add_data()



    book = Book(
        title  ='Deep learning',
        author = 'Ian Goodfellow',
        pages = 775, 
        published = datetime(2016 ,11, 18),
        price = 1500)
    with session_scope()as s:
        s.add(book)
    
    load_yaml(f_yam)
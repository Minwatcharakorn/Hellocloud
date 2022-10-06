from crud import Session
from models2  import Book

s = Session()


bps  = s.query(Book.title ,Book.author).all()
for bp in bps:
    print('Title',bp.title)
    print('Author',bp.author)
    print('_______'*20)


s.close()
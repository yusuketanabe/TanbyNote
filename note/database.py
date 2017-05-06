from sqlalchemy import create_engine, Column, Integer, String, Text 
from datetime import datetime, date
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

database_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'note.db')
engine = create_engine('sqlite:///' + database_file, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Memo(Base): # pattern 1, post data used Python
    __tablename__ = 'notebook'
    id = Column(Integer, primary_key=True)
    title = Column(String(140), unique=True)
    body = Column(Text(140))
    date = Column(String, default=datetime.now().strftime('%Y-%m-%d %H:%M'))

    def __init__(self, title=None, body=None, date=None):
        self.title = title
        self.body = body
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)

def init_db(): # database initialize -> auto run by running 'note.py'
    Base.metadata.create_all(bind=engine)

import logging
import psycopg2
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

log = logging.getLogger(__name__)

path = "postgresql+psycopg2://localhost/postgres"
engine = create_engine(path, echo=True)
metadata = MetaData(bind=engine)
Base = declarative_base(metadata=metadata)


class Words(Base):

    __tablename__ = 'words'

    id = Column(Integer, primary_key=True)
    text = Column(String)

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return "<Words(text='%s')>" % (self.text)


class Database:


    def __init__(self):
        if not database_exists(engine.url):
            create_database(engine.url)
            log.info('База данных создана')
            print('База данных создана')

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_word(self, word):
        word_inst = Words(text=word)
        self.session.add(word_inst)
        self.session.commit()

    def show_words(self):
        result = self.session.query(Words.text).all()
        self.session.commit()
        return result
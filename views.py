from sqlalchemy import create_engine, MetaData
from flask import g
from db import set_address
from app import  app


def chain():
    engine = create_engine(set_address('Data.txt'))
    return engine


with app.app_context():
    db = g.engine = chain()
    meta = MetaData()
    meta.reflect(bind=db)
    users_table = meta.tables['users']
    for row in users_table:
        print("user:", row)

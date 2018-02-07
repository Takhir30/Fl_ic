from sqlalchemy import MetaData, Table
from flask import g
from app import  app, chain


with app.app_context():
    db = g.engine = chain()
    meta = MetaData(bind=db)
    users_table = Table('users', meta, autoload=True)
    for row in users_table:
        print("user:", row)

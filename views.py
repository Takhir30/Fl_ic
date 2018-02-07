from sqlalchemy import MetaData, Table
from sqlalchemy.sql import select
from flask import g
from app import  app, chain


with app.app_context():
    db = g.engine = chain()
    meta = MetaData(bind=db)
    conn = db.connect()
    users_table = Table('users', meta, autoload=True)
    s = select([users])
    result = conn.execute(s)
    for row in result:
        print("user:", row)

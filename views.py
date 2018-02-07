from sqlalchemy import create_engine
from app import chain
from flask import g

def chain():
    engine = create_engine(set_address('Data_text'))
    return engine

db = g.engine = chain()
connection = db.connect()
result = connection.execute()
for row in result:
    print("user:", row)
connection.close()

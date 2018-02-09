from sqlalchemy import Table, MetaData
from sqlalchemy.sql import select
from app import app, get_db


with app.app_context():
    engine = get_db()
    meta = MetaData(bind=engine)
    users = Table('users', meta, autoload=True)
    conn = engine.connect
    s = select([users])
    result = conn.execute(s)
    for row in result:
        print("user:", row)

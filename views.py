from sqlalchemy import Table
from sqlalchemy.sql import select
from app import app, chain_1


with app.app_context():
    meta, conn = chain_1()
    users_table = Table('users', meta, autoload=True)
    s = select([users])
    result = conn.execute(s)
    for row in result:
        print("user:", row)

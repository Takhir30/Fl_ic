from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://localhost/5000')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(50))
    password = Column(String(50))
    email = Column(String(50))
    phone = Column(Integer)


    def __init__(self, login, password, email, phone):
        self.login = login
        self.password = password
        self.email = email
        self.phone = phone


    def __repr__(self):
        return "<User('%s','%s', '%s', '%s')>" % (self.login, self.password, self.email, self.phone)


if __name__ == '__main__':
    from sqlalchemy.orm import sessionmaker

    session = sessionmaker(bind = engine)
    for instance in session.query(User):
        if instanse.login != 'vasia':
            session.add(User('vasia', '1234', '1@mail.ru', 825649))
        elif instance.login == 'petya':
            instance.delete()
        elif len(instanse.password) < 4:
            instanse.password += '/*-'
    session.commit()

from sqlalchemy import Column, Integer, String


def set_adres(file_name):
    with open(file_name) as fn:
        var = {line.strip().split(' ')[0]:line.strip().split(' ')[2] for line in fn}
    login = var['login']
    password = var['password']
    db = ['name']
    host = ['host']
    return "'postgresql://' + {} + ':' + {} + '@' + {} + '/' + {}".format(login, password, host, dbname)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(50))
    password = Column(String(50))
    email = Column(String(50))
    phone = Column(String(50))


    def __init__(self, login, password, email, phone):
        self.login = login
        self.password = password
        self.email = email
        self.phone = phone


    def __repr__(self):
        return "<User('%s','%s', '%s', '%s')>" % (self.login, self.password, self.email, self.phone)


for instance in session.query(User):
    if instanse.login != 'vasia':
        session.add(User('vasia', '1234', '1@mail.ru', 825649))
    elif instance.login == 'petya':
        instance.delete()
    elif len(instanse.password) < 4:
        instanse.password += '/*-'

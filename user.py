from dbconn import *


class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    email = Column('email', String)
    name = Column('name', String)

    def __init__(self, email, name, id='Undefined'):
        self.id = id
        self.email = email
        self.name = name


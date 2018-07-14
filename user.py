import json

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

    def getUsers():
        users = Session().query(User).all()
        userlist = {}
        for u in users:
            user = {'email': u.email, 'name': u.name}
            userlist[u.id] = user
        json.dumps(userlist)
        return userlist

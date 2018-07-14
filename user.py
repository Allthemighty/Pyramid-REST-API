import json

from dbconn import *


class User(Base):
    __tablename__ = 'users'
    metadata = MetaData()

    users = Table(__tablename__, metadata,
                  Column('id', Integer, primary_key=True),
                  Column('email', String),
                  Column('name', String),
                  )

    def __init__(self, email, name, id='Undefined'):
        self.id = id
        self.email = email
        self.name = name

    def getUsers():
        userlist = Session().query(User).all()
        userdict = {}
        for u in userlist:
            user = {'email': u.email, 'name': u.name}
            userdict[u.id] = user
        json.dumps(userdict)
        return userdict

    def getUser(self):
        user = Session().query(User).filter_by(email=self).first()
        if user is None:
            return 'There\'s no such user in our database.'
        userdict = {'id': user.id, 'email': user.email, 'name': user.name}
        json.dumps(userdict)
        return userdict

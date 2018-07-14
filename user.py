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

    @staticmethod
    def get_users():
        """Retrieve all users in the database."""
        user_list = Session().query(User).all()
        user_dict = {}
        for u in user_list:
            user = {'email': u.email, 'name': u.name}
            user_dict[str(u.id)] = user
        json.dumps(user_dict)
        return user_dict

    def get_user(self):
        """Retrieve an individual user from the database."""
        user = Session().query(User).filter_by(email=self).first()
        if user is None:
            return 'There\'s no such user in our database.'
        user_dict = {'id': str(user.id), 'email': user.email, 'name': user.name}
        json.dumps(user_dict)
        return user_dict

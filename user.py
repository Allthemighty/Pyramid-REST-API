import json

from dbconn import *

session = Session()


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
        user_list = session.query(User).all()
        user_dict = {}
        for u in user_list:
            user = {'email': u.email, 'name': u.name}
            user_dict[str(u.id)] = user
        json.dumps(user_dict)
        return user_dict

    def get_user(self):
        """Retrieve an individual user from the database."""
        user = session.query(User).filter_by(email=self).first()
        if user is None:
            return 'There\'s no such user in our database.'
        user_dict = {'id': str(user.id), 'email': user.email, 'name': user.name}
        json.dumps(user_dict)
        return user_dict

    def post_user(self):
        """Post an user to the database."""
        user_table = User.users
        if isinstance(self, User):
            previous_id = session.query(User.id).order_by(User.id.desc()).first()
            ins = insert(user_table).values(id=previous_id[0] + 1, email=self.email, name=self.email)
            conn.execute(ins)
            return 'User has been successfully posted to the database.'
        else:
            return 'This is not a valid user.'

    def delete_user(self):
        """Deletes an user from the database."""
        user = session.query(User).filter_by(email=self).first()
        if user is None:
            return 'There\'s no such user in our database.'
        session.delete(user)
        session.commit()
        return 'User has been successfully deleted from the database.'

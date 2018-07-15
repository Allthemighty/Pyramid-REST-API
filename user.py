import json

from dbconn import *
import uuid

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
            user_id = uuid.uuid4()
            ins = insert(user_table).values(id=user_id, email=self.email, name=self.name)
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

    def edit_user(self, request_body):
        """Edit an user from the database."""
        response_string = ''
        user = session.query(User).filter_by(email=self).first()
        if user is None:
            return 'There\'s no such user in our database.'
        if 'email' in request_body:
            response_string += 'Email of user successfully edited.\n'
            user.email = request_body['email']
        if 'name' in request_body:
            response_string += 'Name of user successfully edited.\n'
            user.name = request_body['name']
        session.commit()
        return response_string

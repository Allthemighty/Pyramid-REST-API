from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import *
from user import User
from waitress import serve


@view_config(route_name='home')
def home(request):
    """Handle the default request, for when no endpoint is specified."""
    return Response('This is Michael\'s REST API!')


@view_config(renderer='json', route_name='users')
def get_users(request):
    """Handle the request to retrieve users."""
    users = User.get_users()
    return Response(str(users))


@view_defaults(renderer='json', route_name='user')
class UserView(object):
    """Handles all requests on the /user endpoint."""

    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET')
    def get(self):
        """Handles the request to retrieve an user by email."""
        response = self.request.matchdict['email']
        user = User.get_user(response)
        return Response(str(user))

    @view_config(request_method='POST')
    def post(self):
        """Handles the request to post an user to the database by email and name."""
        return Response('post')

    @view_config(request_method='PUT')
    def put(self):
        """Handles the request to edit an users data."""
        return Response('put')

    @view_config(request_method='DELETE')
    def delete(self):
        """Handles the request to delete an user from the database."""
        return Response('delete')


if __name__ == '__main__':
    config = Configurator()
    config.add_route('home', '/')
    config.add_route('users', '/users')
    config.add_route('user', '/user/{email}')
    config.scan()
    app = config.make_wsgi_app()
serve(app, host='0.0.0.0', port=1212)

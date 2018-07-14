import json

from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import *
from waitress import serve


def hello_world(request):
    print('Incoming request')
    return Response('This is Michael\'s REST API!')


@view_defaults(renderer='json', route_name='user')
class USERView(object):
    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET')
    def get(self):
        return Response('get')

    @view_config(request_method='POST')
    def post(self):
        return Response('post')

    @view_config(request_method='PUT')
    def put(self):
        return Response('put')

    @view_config(request_method='DELETE')
    def delete(self):
        return Response('delete')


if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    config.add_route('user', '/user')
    config.scan()
    app = config.make_wsgi_app()
serve(app, host='0.0.0.0', port=1212)

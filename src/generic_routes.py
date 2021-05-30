from . import app
from flask import make_response, request
from .models.route_manager import RouteManager

manager = RouteManager()

@app.route('/mock/<path:subpath>')
def routing_handler(subpath):
    route_data = manager.mock_for_path(subpath, request.method, request.data, request.args)
    return make_response(route_data.response_payload, route_data.response_code)

@app.route('/wellcome')
def welcome():
    return "hello! you can access your mocked routes by using /mocks/<your-sub-path>"

@app.errorhandler(404)
def not_a_mock(path):
    route_data = manager.route_not_found()
    return make_response(route_data.response_payload, route_data.response_code)


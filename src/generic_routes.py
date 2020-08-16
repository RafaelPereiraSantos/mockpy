from . import app
from flask import make_response, request
from .models.route_manager import RouteManager
from .models.route_data import RouteData

manager = RouteManager()

@app.route('/hi_there')
def welcome():
    return "hello! you can access your mock routes by using /mocks/<your-sub-path>"

@app.route('/routes', methods=['GET'])
def all_routes():
    response_payload = { "routes": manager.all_raw_routes() }
    return make_response(response_payload, 200)

@app.route('/route/<route_path>', methods=['GET'])
def route_by_name(route_path):
    response_payload = manager.raw_route("/" + route_path)
    return make_response(response_payload, 200)

@app.route('/route', methods=['POST'])
def create_route():
    body = request.json

    try:
        RouteData(body)
    except TypeError as e:
        return str(e)

    manager.reload()
    return "route created"

@app.route("/route/<route_name>/delete", methods=['POST'])
def delete_route_by_name(route_name):
    manager.reload()
    return "route deleted"


@app.route('/mock/<path:subpath>')
def handle_mocked_route(subpath):
    route_data = manager.mock_for_path(subpath, request.method, request.data, request.args)
    return make_response(route_data.response_payload, route_data.response_code)


@app.errorhandler(404)
def not_a_mock(path):
    route_data = manager.route_not_found()
    return make_response(route_data.response_payload, route_data.response_code)


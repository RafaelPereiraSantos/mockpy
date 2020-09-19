from . import app
from flask import make_response, request
from .models.route_manager import RouteManager
from .models.route_data import RouteData

manager = RouteManager()

@app.route('/hi-there')
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

    errors = validate_route_params(body)

    if len(errors) > 0:
        return make_response(format_error_messages(errors), 400)

    path = body['path']

    if manager.has_route(path):
        return make_response(format_error_message('path already used for another route'), 400)

    method = body['method']
    valid_methods = ['GET', 'POST', 'PUT', 'DELETE']

    if not(method in valid_methods):
        return make_response(format_error_message("invalid parameter 'method'"), 400)

    response_payload = body['response_payload']
    response_code = body['response_code']

    try:
        manager.add_new_route(RouteData(path, method, response_payload, response_code))
    except TypeError as e:
        return str(e)

    # manager.reload()
    return "route created"

@app.route("/route/<route_name>", methods=['DELETE'])
def delete_route_by_name(route_name):
    route = '/' + route_name
    if not(manager.has_route(route)):
        return make_response('route not found', 404)
    manager.remove_route(route)
    # manager.reload()
    return make_response('', 204)


@app.route('/mock/<path:subpath>')
def handle_mocked_route(subpath):
    route_data = manager.mock_for_path(subpath, request.method, request.data, request.args)
    return make_response(route_data.response_payload, route_data.response_code)


@app.errorhandler(404)
def not_a_mock(path):
    route_data = manager.route_not_found()
    return make_response(route_data.response_payload, route_data.response_code)

def validate_route_params(body):
    mandatory_params = ['path', 'method', 'response_payload', 'response_code']
    errors = []
    for param_name in mandatory_params:
        if not(param_name in body):
            errors.append(f'missing parameter: {param_name  }')
    return errors

def format_error_message(error):
    return format_error_messages([error])

def format_error_messages(errors):
    return { 'errors': errors }


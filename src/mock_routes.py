from . import app
from flask import make_response, request, render_template
from .models.route_service import RouteService
from .models.route_data import RouteData

manager = RouteService()

@app.route('/routes', methods=['GET'])
def all_routes():
    response_payload = { "routes": manager.all_raw_routes() }
    return make_response(response_payload, 200)

@app.route('/routes/<route_path>', methods=['GET'])
def route_by_name(route_path):
    if not(manager.route_exists(route_path)):
        return route_not_found_error()
    response_payload = manager.raw_route(route_path)
    return make_response(response_payload, 200)

@app.route('/routes', methods=['POST'])
def create_route():
    body = request.json

    errors = validate_route_creation_params(body)

    if len(errors) > 0:
        missing_parameters = ", ".join(errors)
        return error_message("missing parameters: [" + missing_parameters + "]" )

    path = body['path']

    if manager.has_route(path[1:]):
        return route_already_exist_error()

    method = body['method']
    valid_methods = ['GET', 'POST', 'PUT', 'DELETE']

    if not(method in valid_methods):
        return invalid_method_error()

    response_payload = body['response_payload']
    response_code = body['response_code']


    try:
        manager.add_route_with_args(path, method, response_payload, response_code, True)
    except Exception as e:
        print("Error: " + str(e))
        return error_message("oopsy, something really wrong just happend", 500)

    # manager.reload()
    return make_response({ 'message': 'created' }, 201)

@app.route("/route/<route_name>", methods=['DELETE'])
def delete_route_by_name(route_name):
    if not(manager.has_route(route_name)):
        return route_not_found_error()
    manager.remove_route(route_name)
    # manager.reload()
    return make_response('', 204)


@app.route('/mock/<path:subpath>')
def handle_mocked_route(subpath):
    route_data = manager.mock_for_path(subpath, request.method, request.data, request.args)
    return make_response(route_data.response_payload, route_data.response_code)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.errorhandler(404)
def not_a_mock(path):
    route_data = manager.route_not_found()
    return make_response(route_data.response_payload, route_data.response_code)

def validate_route_creation_params(body):
    mandatory_params = ['path', 'method', 'response_payload', 'response_code']
    missing_parameters_list = []
    for param_name in mandatory_params:
        if not(param_name in body.keys()):
            missing_parameters_list.append(param_name)
    return missing_parameters_list

def route_not_found_error():
    return error_message('route does not exist', 404)

def route_already_exist_error():
    return error_message('route already exist', 409)

def invalid_method_error():
    return error_message('invalid HTTP method for route')

def error_message(message, status_code=400):
    print(message)
    return make_response({ 'message': message }, status_code)


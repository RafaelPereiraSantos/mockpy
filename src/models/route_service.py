import json
from os import listdir, remove
from os.path import isfile, join
from .route_data import RouteData

class RouteService():

    RESOURCES_PATH = "./resources"
    JSON_EXTENTION = ".json"

    def __init__(self):
        self.load()

    def reload(self):
        self.load()

    def load(self):
        self.routes = {}
        path = RouteService.RESOURCES_PATH
        for file_name in listdir(path):
            if isfile(join(path, file_name)):
                self.read_and_add_json_mock(file_name)

    def read_and_add_json_mock(self, file_name):
        if file_name.endswith(RouteService.JSON_EXTENTION):
            file_path = RouteService.RESOURCES_PATH + "/" + file_name
            file = open(file_path, "r")
            file_body = json.loads(file.read())
            self.add_route_with_args(
                file_body["path"],
                file_body["method"],
                file_body["response_payload"],
                int(file_body["response_code"])
            )

    def save_new_json_mock(self, route):
        new_file = open(RouteService.RESOURCES_PATH + route.path + RouteService.JSON_EXTENTION, "x")
        raw_json = json.JSONEncoder().encode(route.__dict__)
        print(raw_json)
        new_file.write(raw_json)
        new_file.close()


    def add_route_with_args(self, path, method, response_payload={}, response_code=200, is_a_new_route=False):
        route = RouteData(path, method, response_payload, response_code)
        if (is_a_new_route):
            self.save_new_json_mock(route)
        self.add_new_route(route)

    def add_new_route(self, new_route):
        self.routes[new_route.path[1:]] = new_route

    def has_route(self, path):
        return path in self.routes

    def remove_route(self, path):
        self.routes.pop(path)
        remove(RouteService.RESOURCES_PATH + "/" + path + RouteService.JSON_EXTENTION)

    def mock_for_path(self, path, method, params={}, body={}):
        if self.route_exists(path):
            route = self.routes[path]
            if route.method == method:
                return route
        else:
            return self.route_not_found()

    def raw_route(self, path):
        if self.route_exists(path):
            return self.routes[path].__dict__
        return {}

    def all_raw_routes(self):
        dump = []
        for _, route in self.routes.items():
            dump.append(route.__dict__)
        return dump

    def route_exists(self, path):
        paths = []
        for route in self.routes.keys():
            paths.append(route)
        return path in paths

    def route_not_found(self):
        return self.routes["404"]

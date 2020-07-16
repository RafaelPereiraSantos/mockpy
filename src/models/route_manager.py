import json
from os import listdir
from os.path import isfile, join
from .route_data import RouteData

class RouteManager():

    RESOURCES_PATH = "./resources"

    def __init__(self):
        self.routes = {}
        path = RouteManager.RESOURCES_PATH
        for file_name in listdir(path):
            if isfile(join(path, file_name)):
                self.read_and_add_json_mock(file_name)

    def read_and_add_json_mock(self, file_name):
        if file_name.endswith(".json"):
            file_path = RouteManager.RESOURCES_PATH + "/" + file_name
            file = open(file_path, "r")
            file_body = json.loads(file.read())
            self.add_route(
                file_body["route"],
                file_body["method"],
                file_body["response_payload"],
                int(file_body["code_status"])
            )

    def add_route(self, path, method, response_payload={}, response_code=200):
        self.routes[path] = RouteData(method, response_payload, response_code)

    def mock_for_path(self, path, method, params={}, body={}):
        if path in self.routes:
            route = self.routes[path]
            if route.method == method:
                return route
        else:
            return self.route_not_found()

    def route_not_found(self):
        return self.routes["/404"]

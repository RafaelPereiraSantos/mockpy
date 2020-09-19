class RouteData():
    def __init__(self, path, method, response_payload, response_code):
        self.path = path
        self.method = method
        self.response_payload = response_payload
        self.response_code = response_code

    def export_to_resource(self):
        pass

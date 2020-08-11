class RouteData():
    def __init__(self, route, method, response_payload, response_code):
        self.method = method
        self.response_payload = response_payload
        self.response_code = response_code

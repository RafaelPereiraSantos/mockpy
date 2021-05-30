from . import app

@app.route('/wellcome')
def welcome():
    return "hello! you can access your mocked routes by using /mocks/<your-sub-path>"
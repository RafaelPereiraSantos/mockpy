from flask import Flask
app = Flask(__name__)

from . import routes, mock_routes, static_routes

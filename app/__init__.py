from flask import Flask
from flask_bootstrap import Bootstrap

mywebsite = Flask(__name__,  static_url_path='/app/static')
bootstrap = Bootstrap(mywebsite)


import app.routes

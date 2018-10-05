from flask import Flask
from flask_caching import Cache


App = Flask(__name__)

cache = Cache(App, config={'CACHE_TYPE': 'simple'})

from Routes import *
from runTests import *

if __name__ == "__main__":
    App.run(port=80)


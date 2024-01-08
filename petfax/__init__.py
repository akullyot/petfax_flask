#Import in all dependencies
from flask import Flask

def create_app():
    app = Flask(__name__)
    #creating an index route
    @app.route('/') #decorator to add functionality to the route method
    def index():
        return 'Welcome to petfax'
    @app.route('/pets')
    def show_pets():
        return "These are our pets available for adoption"
    return app
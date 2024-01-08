#Import in all dependencies
from flask import (Flask, render_template)


def create_app(): 
    app = Flask(__name__)
    @app.route('/', methods=['GET']) #methods is a tuple, can be multiple things
    def hello(): 
        return render_template('index.html')
    #import in and register all blueprints
    from . import pet
    app.register_blueprint(pet.pets)
    from . import fact
    app.register_blueprint(fact.facts)

    return app

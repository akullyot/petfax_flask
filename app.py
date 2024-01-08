#Configuration and importing
from flask import Flask #importing in only the flask class
app = Flask(__name__) # pass flask the special dunder variable to instantiate

#creating an index route
@app.route('/') #decorator to add functionality to the route method
def index():
    return 'Welcome to petfax'


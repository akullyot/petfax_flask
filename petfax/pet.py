
from flask import (Blueprint, render_template)
import json


pets = Blueprint('pets', __name__, url_prefix="/pets")
pet_json = json.load(open('pets.json'))

@pets.route('/')
def show_pets():
    return render_template(
        "pets/show_pets.html",
        pets_json = pet_json
    )
#dynamic routes
@pets.route('/<int:pet_id>') #sepcifying data type here forces type
def show_pet(pet_id):
    pet = pet_json[pet_id - 1]
    return render_template('pets/show_pet.html', pet=pet)
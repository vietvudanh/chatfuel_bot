import json

from flask import current_app, Blueprint, render_template, jsonify
general = Blueprint('general', __name__)


@general.route('/')
def index():
    data = None
    with open('lunch/data/places.json', 'r') as f:
        data = json.load(f)

    return jsonify(
        data=data
    )

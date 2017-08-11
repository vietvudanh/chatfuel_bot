# -*- coding: utf-8 -*-
import json
import random

from flask import current_app, Blueprint, render_template, jsonify
general = Blueprint('general', __name__)


@general.route('/')
def index():
    data = None
    with open('lunch/data/places.json', 'r') as f:
        data = json.load(f)
    places = data['places']

    total = sum([p['priority'] for p in places])
    r = random.uniform(0, total)

    # random with weight
    choice = None
    up_to = 0
    for place in places:
        if up_to + place['priority'] >= r:
            choice = place
            break
        up_to += place['priority']

    return jsonify({
        'message': {
            'text': "Địa điểm: " + choice['name'],
            'text': "Khoảng cách: " + str(choice['priority']),
        }
    })

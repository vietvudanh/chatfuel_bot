# -*- coding: utf-8 -*-
import json
import random

from flask import current_app, Blueprint, jsonify
general = Blueprint('general', __name__)


@general.route('/choice')
def choice():
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
        'messages': [{
            'text': "Địa điểm: " + choice['name'] + "\n"
                    + "Khoảng cách: " + choice['name'] + "\n"
                    + "Ưu tiên: " + choice['priority'] + "\n"
        }]
    })

@general.route('/')
def index():
    data = None
    with open('lunch/data/places.json', 'r') as f:
        data = json.load(f)
    places = data['places']

    return jsonify({
        'messages': [{'text': "Tất cả các địa điểm"}] 
        + [{
            'text': "Địa điểm: " + place['name'] + "\n"
                    + "Khoảng cách: " + place['name'] + "\n"
                    + "Ưu tiên: " + place['priority'] + "\n"
        } for place in places]
    })

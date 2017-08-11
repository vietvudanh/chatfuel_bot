# -*- coding: utf-8 -*-
import json
import random

from flask import current_app, Blueprint, jsonify
general = Blueprint('general', __name__)

def repr(place):
    return "Địa điểm: " + str(place['name'].encode('utf-8')) + "\n" + "Khoảng cách: " + str(place['distance']) + "\n" + "Ưu tiên: " + str(place['priority'])


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
            'text': repr(choice)
        }]
    })


@general.route('/')
def index():
    data = None
    with open('lunch/data/places.json', 'r') as f:
        data = json.load(f)
    places = data['places']

    return jsonify({
        'messages':
            [{'text': "Tất cả các địa điểm"}]
            +
            [{'text': repr(place)} for place in places]
    })

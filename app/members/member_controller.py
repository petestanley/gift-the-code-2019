import http
import random

import flask
from flask_cors import cross_origin


members = flask.Blueprint('members', __name__, url_prefix='/members')


@members.route('/<member_id>', methods=['GET'])
def get(member_id):
    response_body = {
        "id": member_id,
        "email": 'john.smith@movember.com',
        "mopoints": 42,
        "firstName": "John",
        "lastName": "Smith"
    }
    response = flask.jsonify(response_body)
    response.status_code = http.HTTPStatus.OK
    return response


@members.route('/', methods=['POST'])
def post():
    request_data = flask.request.json
    first_name = request_data.get('firstName', '')
    last_name = request_data.get('lastName', '')
    email = request_data.get('email', '')
    member_id = random.randint(1, 100)

    response_body = {
        "id": member_id,
        "email": email,
        "mopoints": 0,
        "firstName": first_name,
        "lastName": last_name
    }
    response = flask.jsonify(response_body)
    response.status_code = http.HTTPStatus.CREATED
    return response

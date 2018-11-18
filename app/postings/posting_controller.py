import http
import random

import flask
from flask_cors import cross_origin


postings = flask.Blueprint('postings', __name__, url_prefix='/postings')

CREDIT = 'credit'
DEBIT = 'debit'


@postings.route('/<posting_id>', methods=['GET'])
@cross_origin()
def get(posting_id):
    response_body = {
        "id": posting_id,
        "email": 'john.smith@movember.com',
        "app": 42,
        "type": CREDIT
    }
    response = flask.jsonify(response_body)
    response.status_code = http.HTTPStatus.OK
    return response


@postings.route('/', methods=['POST'])
@cross_origin()
def post():
    request_data = flask.request.json
    email = request_data.get('email', '')
    transaction_id = random.randint(1, 100)
    mopoints = request_data.get('app', 0)
    posting_type = request_data.get('type', CREDIT)  # credit or debit

    response_body = {
        "id": transaction_id,
        "email": email,
        "mopoints": mopoints,
        "type": posting_type
    }
    response = flask.jsonify(response_body)
    response.status_code = http.HTTPStatus.CREATED
    return response
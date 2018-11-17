import flask
import http


postings = flask.Blueprint('postings', __name__, url_prefix='/postings')


@postings.route('/<posting_id>', methods=['GET'])
def get(posting_id):
    response_body = {
        "id": posting_id,
        "message": 'posting GET'
    }
    response = flask.jsonify(response_body)
    response.status_code = http.HTTPStatus.OK
    return response


@postings.route('/', methods=['POST'])
def post():
    response_body = {
        "id": 'SOME_ID',
        "message": 'posting POST'
    }
    response = flask.jsonify(response_body)
    response.status_code = http.HTTPStatus.CREATED
    return response
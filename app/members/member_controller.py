import flask
import http


members = flask.Blueprint('members', __name__, url_prefix='/members')


@members.route('/<member_id>', methods=['GET'])
def get(member_id):
    response_body = {
        "id": member_id,
        "message": 'member GET'
    }
    response = flask.jsonify(response_body)
    response.status_code = http.HTTPStatus.OK
    return response


@members.route('/', methods=['POST'])
def post():
    response_body = {
        "id": 'SOME_ID',
        "message": 'member POST'
    }
    response = flask.jsonify(response_body)
    response.status_code = http.HTTPStatus.CREATED
    return response
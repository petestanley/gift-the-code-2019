# Import flask and template operators
import flask
import flask_cors
import http

from app.postings.posting_controller import postings
from app.members.member_controller import members

# Define the WSGI application object
app = flask.Flask(__name__)
flask_cors.CORS(app)

# Configurations
app.config.from_object('config')


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return '', http.HTTPStatus.NOT_FOUND


@app.route('/', methods=['GET'])
def index():
    return "Mo money, mo problems."


app.register_blueprint(postings)
app.register_blueprint(members)

import os


# Statement for enabling the development environment
DEBUG = True

SEND_FILE_MAX_AGE_DEFAULT = 0

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# Google Cloud Services Config
PROJECT_ID = 'gift-the-code-api'

DATA_BACKEND = 'cloudsql'
CLOUDSQL_USER = 'root'
CLOUDSQL_PASSWORD = 'points123'
CLOUDSQL_DATABASE = 'app'
CLOUDSQL_CONNECTION_NAME = 'gift-the-code-222817:us-central1:app-db'

LIVE_SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{user}:{password}@localhost/{database}'
    '?unix_socket=/cloudsql/{connection_name}').format(
        user=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD,
        database=CLOUDSQL_DATABASE, connection_name=CLOUDSQL_CONNECTION_NAME)

SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI

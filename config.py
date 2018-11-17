import os


# Statement for enabling the development environment
DEBUG = True

SEND_FILE_MAX_AGE_DEFAULT = 0

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# Google Cloud Services Config
DATABASE_URL = ''
TRANSACTIONS_TABLE = ''
USERS_TABLE = ''

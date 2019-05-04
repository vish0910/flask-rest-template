from flask import Blueprint
from flask_restplus import Api
from settings.version import __VERSION__

blueprint = Blueprint('api', __name__)
api = Api(
    blueprint, version=__VERSION__, title='API Title', validate=True,
    description='This is a template API',
)

# DO NOT MOVE THIS IMPORT - Because 'api' is defined above, we dont have access to it at the top. pep8 disabled.
from api.v1 import endpoints  # nopep8

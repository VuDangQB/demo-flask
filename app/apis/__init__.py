from flask import (
    Blueprint
)
blueprint = Blueprint('api', __name__, url_prefix='/')

@blueprint.route('/')
def hello():
    return 'Hello, World!'
from datetime import datetime
from socket import gethostname

from flask import jsonify, make_response, Response
from config import flask_app


@flask_app.route('/')
def default_route() -> Response:
    return make_response('default route', 200)


@flask_app.route('/health', strict_slashes=False)
def health_check() -> Response:
    now = datetime.utcnow()

    return jsonify(
        {
            'time': str(now),
            'ts': now.timestamp(),
            'service_name': 'challenge_starter',
            'hostname': gethostname(),
            'status': 'allgood',
            'components': []
        }
    )

import os
import yaml
import flask
from decorator import decorator


def _read_config():
    project_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 1)[0]
    config_path = os.path.join(project_dir, 'api.conf')
    conf = {}
    if os.path.exists(config_path):
        with open(config_path) as config_file:
            conf = yaml.load(config_file)
    return conf


def _check_key(api_key):
    keys = _read_config().get('API').get('keys', [])
    if api_key in keys:
        return True
    return False


def _auth_error(msg):
    return flask.Response(
        msg,
        401
    )


@decorator
def requires_token(fun, *args, **kwargs):
    api_key = flask.request.headers.get('API-Key', None)
    if not api_key:
        return _auth_error('Missing API-Key')
    authenticated = _check_key(api_key)
    if not authenticated:
        return _auth_error('Key not accepted')
    return fun(*args, **kwargs)


if __name__ == '__main__':
    conf = _read_config()

    print(os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2))
    #print(_check_key(123))
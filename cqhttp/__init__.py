from collections import defaultdict
from functools import wraps

import requests

from bottle import Bottle, request, abort


class Error(Exception):
    def __init__(self, status_code, retcode=None):
        self.status_code = status_code
        self.retcode = retcode


class _ApiClient(object):
    def __init__(self, api_root=None, token=None):
        self.url = api_root.rstrip('/') if api_root else None
        self.token = token

    @property
    def auth(self):
        return 'token ' + self.token if self.token else None

    def __getattr__(self, item):
        if self.url:
            c = _ApiClient(api_root=self.url + '/' + item, token=self.token)
            return c

    def __call__(self, *args, **kwargs):
        resp = requests.post(self.url, json=kwargs,
                             headers={'Authorization': self.auth})
        if resp.ok:
            data = resp.json()
            if data.get('status') == 'ok':
                return data.get('data')
            raise Error(resp.status_code, data.get('retcode'))
        raise Error(resp.status_code)


def _deco_maker(post_type):
    def deco_decorator(self, *types):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            if types:
                for t in types:
                    self.handlers[post_type][t] = wrapper
            else:
                self.handlers[post_type]['*'] = wrapper
            return wrapper

        return decorator

    return deco_decorator


class CQHttp(_ApiClient):
    def __init__(self, api_root=None, token=None):
        super().__init__(api_root, token)
        self.handlers = defaultdict(dict)
        self.app = Bottle()
        self.app.post('/')(self.handle)

    on_message = _deco_maker('message')
    on_event = _deco_maker('event')
    on_request = _deco_maker('request')

    def handle(self):
        if self.auth and request.headers.get('Authorization') != self.auth:
            abort(401)

        post_type = request.json.get('post_type')
        if post_type not in ('message', 'event', 'request'):
            abort(400)

        handler_key = None
        for pk_pair in (('message', 'message_type'),
                        ('event', 'event'),
                        ('request', 'request_type')):
            if post_type == pk_pair[0]:
                handler_key = request.json.get(pk_pair[1])
                if not handler_key:
                    abort(400)
                else:
                    break

        if not handler_key:
            abort(400)

        handler = self.handlers[post_type].get(handler_key)
        if not handler:
            handler = self.handlers[post_type].get('*')  # try wildcard handler
        if handler:
            assert callable(handler)
            return handler(request.json)
        return ''

    def run(self, host=None, port=None, **kwargs):
        self.app.run(host=host, port=port, **kwargs)

    def send(self, context, message, **kwargs):
        if context.get('group_id'):
            return self.send_group_msg(group_id=context['group_id'],
                                       message=message, **kwargs)
        elif context.get('discuss_id'):
            return self.send_discuss_msg(discuss_id=context['discuss_id'],
                                         message=message, **kwargs)
        elif context.get('user_id'):
            return self.send_private_msg(user_id=context['user_id'],
                                         message=message, **kwargs)

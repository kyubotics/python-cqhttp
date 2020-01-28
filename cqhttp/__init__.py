import hmac
from collections import defaultdict
from functools import wraps
from typing import Callable

import requests
from flask import Flask, request, abort, jsonify


class Error(Exception):
    def __init__(self, status_code, retcode=None):
        self.status_code = status_code
        self.retcode = retcode


def _api_client(url, access_token=None):
    def do_call(**kwargs):
        headers = {}
        if access_token:
            headers['Authorization'] = 'Token ' + access_token
        resp = requests.post(url, json=kwargs, headers=headers)
        if resp.ok:
            data = resp.json()
            if data.get('status') == 'failed':
                raise Error(resp.status_code, data.get('retcode'))
            return data.get('data')
        raise Error(resp.status_code)

    return do_call


def _deco_maker(type_):
    def deco_deco(self, arg=None, *detail_types):
        def deco(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            if isinstance(arg, str):
                for detail_type in [arg] + list(detail_types):
                    self._handlers[type_][detail_type] = wrapper
            else:
                self._handlers[type_]['*'] = wrapper
            return wrapper

        if isinstance(arg, Callable):
            return deco(arg)
        return deco

    return deco_deco


class CQHttp:
    def __init__(self, api_root=None, access_token=None, secret=None):
        self._api_root = api_root.rstrip('/') if api_root else None
        self._access_token = access_token
        self._secret = secret
        self._handlers = defaultdict(dict)
        self._server_app = Flask(__name__)
        self._server_app.route('/', methods=['POST'])(self._handle)

    @property
    def wsgi(self):
        return self._server_app

    @property
    def server_app(self):
        return self._server_app

    @property
    def logger(self):
        return self._server_app.logger

    on_message = _deco_maker('message')
    on_notice = _deco_maker('notice')
    on_request = _deco_maker('request')
    on_meta_event = _deco_maker('meta_event')

    def _handle(self):
        if self._secret:
            if 'X-Signature' not in request.headers:
                abort(401)

            sec = self._secret
            sec = sec.encode('utf-8') if isinstance(sec, str) else sec
            sig = hmac.new(sec, request.get_data(), 'sha1').hexdigest()
            if request.headers['X-Signature'] != 'sha1=' + sig:
                abort(403)

        event = request.json
        type_ = event.get('post_type', '')
        detail_type = event.get('{}_type'.format(type_), '')
        if not detail_type:
            abort(400)

        self.logger.info('received event: ' + type_ + '.' + detail_type)

        handler = self._handlers[type_].get(detail_type,
                                            self._handlers[type_].get('*'))
        if handler:
            response = handler(event)
            return jsonify(response) if isinstance(response, dict) else ''
        return ''

    def run(self, host=None, port=None, **kwargs):
        self._server_app.run(host=host, port=port, **kwargs)

    def send(self, event, message, **kwargs):
        params = event.copy()
        params['message'] = message
        params.pop('raw_message', None)  # avoid wasting bandwidth
        params.pop('comment', None)
        params.pop('sender', None)
        params.update(kwargs)
        if 'message_type' not in params:
            if 'group_id' in params:
                params['message_type'] = 'group'
            elif 'discuss_id' in params:
                params['message_type'] = 'discuss'
            elif 'user_id' in params:
                params['message_type'] = 'private'
        return self.send_msg(**params)

    def __getattr__(self, item):
        if self._api_root:
            return _api_client(self._api_root + '/' + item, self._access_token)

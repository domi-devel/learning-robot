# from robotcontrol import app as app
# from app import create_app
import robotcontrol
from robotcontrol import app
from robotcontrol import manage
from robotcontrol.app import create_app
import unittest


# How to run this file ?
# Go to the flask-quickstart directory
# ie. the directory above this one
# and execuute the following from the terminal
# python -m unittest tests.test_main

# ../flask-quickstart$ python -m unittest tests.test_main

# You IDE / editor will most likely have a feature/extension
# that automatically discovers and runs tests.


def test_main():
    app = create_app('testing')
    client = app.test_client()
    rv = client.get('/')
    assert rv.status == '200 OK'


def test_load():
    app = create_app('testing')
    client = app.test_client()
    rv = client.get('/load')
    assert rv.status == '200 OK'


def test_save():
    app = create_app('testing')
    client = app.test_client()
    rv = client.get('/save')
    assert rv.status == '200 OK'


def test_404():
    app = create_app('testing')
    client = app.test_client()
    rv = client.get('/unknownendpoint')
    assert rv.status == '404 NOT FOUND'


def test_post():
    app = create_app('testing')
    client = app.test_client()
    rv = client.post('/post', data='load3')
    assert rv.data == b'OK'
    rv = client.post('/post', data='save1')
    assert rv.data == b'OK'
    rv = client.post('/post', data='train')
    assert rv.data == b'OK'
    rv = client.post('/post', data='work')
    assert rv.data == b'OK'
    rv = client.post('/post', data='idle'.encode())
    assert rv.data == b'OK'
    rv = client.post('/post', data='no\n')
    assert rv.data == b'NOK'

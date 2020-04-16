import pytest
from robotinterfaces import hello_world

def test_hello_world():
    response = hello_world()
    assert 'Hello world' == response
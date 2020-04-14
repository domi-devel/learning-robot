import pytest
from  learning_robot.robot_interfaces import i2c_devices

def test_hello_world():
    response = i2c_devices.hello_world()
    assert 'Hello world' == response
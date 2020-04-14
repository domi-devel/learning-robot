# Tests
Verwendung von `pytest` als Test-Library

## FakeRPi
Für Testen von I²C-Funktionen Verwendung von FakeRPi-Library (https://github.com/MomsFriendlyRobotCompany/fake_rpi )

Verwendung:
```python
# -*- coding:utf-8 -*-
# Replace libraries by fake ones
import sys
if sys.platform == "win32":
    import fake_rpi

    fake_rpi.toggle_print(False)
    sys.modules["RPi"] = fake_rpi.RPi  # Fake RPi
    sys.modules["RPi.GPIO"] = fake_rpi.RPi.GPIO  # Fake GPIO
    sys.modules["smbus"] = fake_rpi.smbus  # Fake smbus (I2C)
import RPi.GPIO as GPIO
```
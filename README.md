# learning-robot

[![Build Status](https://travis-ci.org/domi-devel/learning-robot.svg?branch=master)](https://travis-ci.org/domi-devel/learning-robot)
[![codecov](https://codecov.io/gh/domi-devel/learning-robot/branch/master/graph/badge.svg)](https://codecov.io/gh/domi-devel/learning-robot)

## Install

```bash
pip install -r requirements.txt
pip install .
```

## Development Setup for code coverage

```bash
pip install -r requirements.txt
pip install -e .
pytest --cov=robotcontrol --cov=machinelearning --cov=robotinterfaces
```

## Run

```bash
python learning_robot/robotcontrol/manage.py runserver --env development --port 8080
```
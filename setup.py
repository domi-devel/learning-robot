  #!/usr/bin/env python

from distutils.core import setup

setup(name='learning_robot',
      version='1.0',
      description='Self-learning robot with machine learning methods',
      author='Students',
      packages=['learning_robot', 'learning_robot.robot_interfaces', 'learning_robot.machine_learning' ],
     )
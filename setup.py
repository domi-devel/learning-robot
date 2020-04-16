  #!/usr/bin/env python

from distutils.core import setup

setup(name='learning_robot',
      version='1.0',
      description='Self-learning robot with machine learning methods',
      author='Students',
      package_dir = {'': 'learning_robot'},
      packages=['robotcontrol', 'robotinterfaces', 'machinelearning' ],
     )
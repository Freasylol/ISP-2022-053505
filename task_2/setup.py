from setuptools import setup

setup(
   name='customSerializer',
   version='1.0',
   description='You can use it for TOML, YAML, JSON and also construct them with fabric',
   author='rom4chick',
   install_requires=['PyYAML', 'toml', 'pytest'],
   packages=['customSerializer'],
)

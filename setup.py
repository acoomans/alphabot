from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
	long_description = f.read()
	
with open(path.join(here, 'requirements.txt')) as f:
	requirements = f.read()

setup(
	name='alphabot-control',
	version=0.1,
	author='Arnaud Coomans',
	author_email='hello@acoomans.com',
	description='Controller for Alphabot',
	long_description=long_description,
	url='https://github.com/acoomans/alphabot-control',
	license='BSD',
	platforms='any',
	install_requires=requirements,
	scripts=['scripts/alphabot-control.py'],
	packages=find_packages(exclude=['contrib', 'docs', 'tests']),
	test_suite='tests.test_project',
)
from setuptools import setup, find_packages
import re

def getVersion():
	with open('myUtils/__init__.py', 'r') as file:
		content = file.read
	match = re.search(r"__version__\s*=\s*'([^']+)'", content)
	if match:
		return match.group(1)
	raise RuntimeError('Version not found.')
	
setup(
    name='myUtils',
	packages=['myUtils'],
    version=getVersion(),
    install_requires=[],
    author='K-Mart',
    description='My utility functions',
    url='https://github.com/Jitzwaz/myUtils',
)
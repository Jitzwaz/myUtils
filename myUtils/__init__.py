import time
import subprocess
import sys
import re
import urllib.request

__version__ = '1.3.11'

def calcTime(func, *args):
	"""
	Calculates the time taken to execute a function.

	Args:
		func (function): The function to be executed.
		args (tuple): The arguments to be passed to the function.

	Returns:
		float: The time taken to execute the function in milliseconds.

	"""
	if args:
		start = time.perf_counter()
		func(*args)
		end = time.perf_counter()
		return (end-start)*1000
	elif not args:
		start = time.perf_counter()
		func()
		end = time.perf_counter()
		return (end-start)*1000
	
def newline(lines: int = 1):
	"""
	Prints a specified number of new lines.

	Args:
		lines (int): The number of new lines to print.

	Returns:
		None
	"""
	try:
		if type(lines) is not int:
			lines = int(lines)
	except ValueError:
		print("Invalid input, please enter an integer.")
		return
	for i in range(lines):
		print("\n", end="")

def debugPrint(debug: bool, *args):
	"""
	Prints the arguments if debug is True.

	Args:
		debug (bool): If True, prints the arguments.
		*args: The arguments to be printed.

	Returns:
		None

	"""
	if debug:
		for arg in args:
			print(arg, end=" ")

def displayDictionary(d: dict):
	"""
	Displays the contents of a dictionary in a more legible way. (line by line)

	Args:
		d (dictionary): The dictionary to be displayed. 

	Returns:
		None 
	"""
	for key, value, in d.items():
		try:
			print(f'{key}: {value}')
		except ValueError:
			print(f'ValueError: {value} is not iterable.')

def invertDictionary(d: dict, debugMode: bool): 
	"""
	Inverts the contents of a dictionary and preserves errors.

	Args: 
		d (dictionary): The dictionary to be inverted 
		debugMode (bool): The debug mode variable or a true/false boolean. 
	
	Returns: 
		inverted dictionary (dictionary) 
		error log (list)
		
	"""
	inverted = {} # Inverted dictionary to be exported
	errors = [] # List to hold errors encountered during inversion.
	for key, value in d.items(): # Iterate through the dictionary.
		for val in value:
			try: # Attempt to use the value as a key in the inverted dictionary.
				if val not in inverted:
					inverted[val] = [] # If the value is not already a key in the inverted dictionary, it will create a new key with an empty list.
				if key not in inverted[val]: # If the key is not already in the list for that value, it will append the key to the list.
					inverted[val].append(key) # Appends the student to the list of students for that course.
			except TypeError: # Catches any TypeErrors caused by the value not being a hashable type (e.g., a list).
				errors.append(f'val: {val}: type:{type(val)} is not hashable') # Add error to the list showing the actual value and it's type.
	if debugMode: # If debug mode is enabled, print the inverted dictionary and any errors encountered.
		if errors:
			print('Errors encountered during inversion:')
			for error in errors: # Iterates through the errors list and prints each error.
				print(error)
		else:
			print('No errors encountered during inversion.')
		print('\n', end='') # Print a new line for improved readability.
		print('Inverted dictionary:')
		return inverted, errors
	else:
		return inverted # Returns the inverted dictionary and no errors if debug mode is not enabled.

def displayList(l: list):
	"""
	Displays the contents of a list in a more legible way.

	Args:
		l (list): The list to be displayed.

	Returns:
		None

	"""
	for val in l:
		print(val)

def getPackageVersion(packageName, username):
	"""
	Retrieves the version number of a package, assuming the version is in the __init__.py file.
	Will print any errors as well as return them for analysis.
	Args:
		packageName (string): The name of the package.
		username (string): The github username of the author in the link.
	Returns:
		Version number (string)
		Exception (Any)
	"""
	url = f'https://raw.githubusercontent.com/{username}/{packageName}/main/{packageName}/__init__.py'
	try:
		with urllib.request.urlopen(url) as response:
			text = response.read().decode('utf-8')
			match = re.search(r"__version__\s*=\s*['\"]([^'\"]+)['\"]", text)
			if match:
				return match.group(1)
	except Exception as e:
		print(f'Failed to fetch version of {packageName}: {end=}')
		return e
	return None

def updatePackage(packageName, username):
	"""
	Updates the specified package via pip.

	Args:
		packageName (string): The name of the package.
		username (string): The github username of the author in the link.
	Returns:
		None
	"""
	subprocess.run([
		sys.executable,
		'-m',
		'pip',
		'install',
		'--upgrade',
		'--no-cache-dir',
		f'git+https://github.com/{username}/{packageName}.git'
	])

def rollbackPackage(packageName, username, version):
	"""
	Reverts the specified packaged to the desired version.

	Args:
		packageName (string): The name of the package.
		username (string): The github username of the author in the link.
		version (string): The version to revert to.
	Returns:
		None
	"""
	subprocess.run([
		sys.executable,
		'-m',
		'pip',
		'install',
		'--upgrade',
		'--no-cache-dir',
		f'git+https://github.com/{username}/{packageName}.git@{version}'
	])
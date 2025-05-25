import time

def calcTime(func, args):
	'''
	Calculates the time taken to execute a function. \n
	Args: \n
		func (function): The function to be executed. \n
		args (tuple): The arguments to be passed to the function. \n
	Returns: \n
		float: The time taken to execute the function in milliseconds. \n
	'''
	if args:
		start = time.perf_counter()
		func(args)
		end = time.perf_counter()
		return (end-start)*1000
	elif not args:
		start = time.perf_counter()
		func()
		end = time.perf_counter()
		return (end-start)*1000
	
def newline(lines=1):
	'''
	Prints a specified number of new lines. \n
	Args: \n
		lines (int): The number of new lines to print. \n
	Returns: \n
		None \n
	'''
	try:
		if type(lines) is not int:
			lines = int(lines)
	except ValueError:
		print("Invalid input, please enter an integer.")
		return
	for i in range(lines):
		print("\n", end="")

def debugPrint(debug, *args):
	'''
	Prints the arguments if debug is True. \n
	Args: \n
		debug (bool): If True, prints the arguments. \n
		*args: The arguments to be printed. \n
	Returns: \n
		None \n
	'''
	if debug:
		for arg in args:
			print(arg, end=" ")

def displayDictionary(d):
	'''
	Displays the contents of a dictionary in a more legible way. \n
	Args: \n
		d (dict): The dictionary to be displayed. \n
	Returns: \n
		None \n
	'''
	for key, value, in d.items():
		print(f'{key}: {", ".join(value)}')

def displayList(l):
	'''
	Displays the contents of a list in a more legible way. \n
	Args: \n
		t (list): The list to be displayed. \n
	Returns: \n
		None \n
	'''
	for val in l:
		print(val)

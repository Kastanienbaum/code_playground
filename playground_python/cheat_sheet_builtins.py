#!/usr/bin/env python2 

'''  
In this file I give some examples for basic python functionalities. This code 
provides a cheat sheet if I forget about some basic python things... 

see also builtin python functions: 
https://docs.python.org/3/library/functions.html

'''



def main():

	def funky():
		pass

	var_int = 42
	var_char = 'c'
	var_str = 'string' 
	var_list = (11, 12, 13, 14, 15, 16) 
	var_dict = {'a': 1, 'b': 2, 'word': var_int}

	# dir() returns list of names in current local scope (in alphabetical order)
	print(dir())

	# dir([object]) returns list of (valid) attributes for an object
	print(dir(var_int))
	print(dir(var_int.__abs__))

	print(dir(var_str))
	print(dir(var_str.__abs__))


if __name__ == '__main__':
	main()


# EOF 


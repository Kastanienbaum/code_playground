#!/usr/bin/env python3 

import argparse 

glob_list = []

def check_list(value):
	#my_list = value 
	#print(my_list)
	print(value)
	#glob_list.append(value)
	#args.fancy_list.append(value)

def main():
	
	parser = argparse.ArgumentParser() 

	parser.add_argument('obligatory_arg')
	parser.add_argument('-l', '--fancy_list', nargs='+', action='append', 
						metavar=('a', 'b')) 
	# action='extend' is only python3 
	parser.add_argument('-a', '--fancy_action', nargs='+', type=check_list) 

	args = parser.parse_args() 

	print('args.fancy_action: ' + str(args.fancy_action))
	print('glob_list:         ' + str(glob_list))
	print('args.fancy_list:   ' + str(args.fancy_list))

if __name__ == '__main__':
	main()

# EOF 

#!/usr/bin/python3 

# https://adventofcode.com/2020/day/1

import itertools

with open('day1_input.txt', 'r') as f:
	numbers = f.readlines()

# part 1 
# solution: 51 + 1969 = 2020 
# 51 * 1969 = 100419

'''for i, x in enumerate(numbers):
	for y in range(len(numbers)-i-1):
		result = int(x) + int(numbers[i+y+1]) 
		if result == 2020:
			print(x + " + " + numbers[i+y+1] + " = " + str(result))
			product = int(x) * int(numbers[i+y+1]) 
			print(product) 
'''
# part 2 

# solution: 483 + 565 + 972 = 2020 
# 483 * 565 * 972 = 265253940 

combs = itertools.combinations(numbers, 3)
for x in combs:
	if (int(x[0]) + int(x[1]) + int(x[2]) == 2020):
		print("sum: " + x[0] + x[1] + x[2])
		prod = int(x[0]) * int(x[1]) * int(x[2])
		print(prod)
		break


# EOF 

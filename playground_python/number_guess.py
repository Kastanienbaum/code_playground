#!/usr/bin/env python3 

import random

print('Please enter a number between 1 and 100!')
print('I will then guess the number!')

number = int(input())
while (int(number) > 100 or int(number) < 1):
	print('invalid range')
	number = int(input())

upper_limit = 100 
lower_limit = 1
possible_range = [lower_limit, upper_limit]
guess = random.randint(lower_limit, upper_limit)

guessed_numbers = []

print('- - - V E R S I O N   1 - - -')
while guess != number:

	while True:
		guess = random.randint(possible_range[0], possible_range[1])

		if not(guess in guessed_numbers):
			break
		
	print('My guess is %d' %guess)

	guessed_numbers.append(guess)

	if guess > number:
		possible_range[1] = guess
	elif guess < number: 
		possible_range[0] = guess
	else: 
		print('The number is %d!' %number)



possible_range = [lower_limit, upper_limit]
guess = random.randint(lower_limit, upper_limit)

guessed_numbers = []

print('- - - V E R S I O N   2 - - -')
while guess != number:

	while True:
		guess = random.randint(possible_range[0], possible_range[1])

		if not(guess in guessed_numbers):
			break
		
	print('My guess is %d' %guess)

	guessed_numbers.append(guess)

	if guess > number:
		possible_range[1] = guess
	elif guess < number: 
		possible_range[0] = guess
	else: 
		print('The number is %d!' %number)



print('Goodbye')
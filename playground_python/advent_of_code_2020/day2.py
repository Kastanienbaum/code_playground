#!/usr/bin/python3 

# https://adventofcode.com/2020/day/1

with open('day2_input.txt', 'r') as f:
	passwords = f.readlines()

# part 1 
# solution: 456 valid entries

valid_pw = 0
entries = 0

for pw_entry in passwords: 
	remainder = pw_entry.split('-')
	min_occurence = int(remainder[0])
	remainder = remainder[1].split(' ', 1)
	max_occurence = int(remainder[0])
	remainder = remainder[1].split(':')
	letter = remainder[0]
	remainder = remainder[1].split('\n')
	pw = remainder[0]

	entries += 1
	char_count = pw.count(letter)
	if not(char_count < min_occurence or char_count > max_occurence):
		valid_pw += 1

print(valid_pw, entries)

# part 2 



# EOF 
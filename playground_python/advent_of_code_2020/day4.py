#!/usr/bin/python3 

import collections 

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

# part 2 
def check_rules(checked):
	if ()


def check_validity(a, b):
	# remove cid from list 
	if 'cid' in a:
		a.remove('cid')
	if collections.Counter(a) == collections.Counter(b):
		check_rules(a)
		return True 
	else: 
		return False


infile = 'day4_input.txt' # 'day4_sample.txt' 

# part 1 

# cid not needed 
valid_credentials = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# this dict is used for part 2 
rules = {'byr': (1920, 2002), 
		 'iyr': (2010, 2020), 
		 'eyr': (2020, 2030), 
		 'hgt': (('cm', 150, 193), ('in', 59, 76)), 
		 'hcl': ('^#[0-9a-fA-F]{6}'), # a '#' followed by exactly six characters in the range of 0-9 or a-f or A-F
		 'ecl': ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'), 
		 'pid': ('[0-9]{9}') # nine-digit number including leading zeroes 
     }


valid_passports = 0

with open(infile, 'r') as f: 
	tmp = []
	remainder = ''
	for i, line in enumerate(f):
		if (line == '\n'):
			# check if all necessary credentials are there
			if check_validity(tmp, valid_credentials):
				valid_passports += 1
			# reset vars
			tmp = []
			remainder = ''
		else: 
			# add credential
			entries = line.split(' ')
			for e in entries:
				tmp.append(e.split(':')[0])

	# check the last entry
	if check_validity(tmp, valid_credentials):
		valid_passports += 1


print('valid passports: '+ str(valid_passports))

# EOF 

#!/usr/bin/env python3 

# print random UNICODE characters 

from random import * 
import unicodedata
import time 

possible_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890^°!"§$%&/()=?`´+*#\'äÄüÜöÖ.:,;-_€@<>|'
letters = 'aAbBcC '

min_printable_char = 0
max_printable_char = 0xFFFF

for x in range(0,1000):
	mystr = ''
	for y in range(0, 100):
		mystr = mystr + (possible_chars[randint(0, len(possible_chars)-1)] + ' ')

	print(mystr + '\n')
	time.sleep(0.1)

#print(u'u\u265E')
	
	#unicode 
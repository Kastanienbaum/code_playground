#!/usr/bin/env python2 

var_a = 0x42 		# type int 
var_b = 0x224466 	
var_c = "\x12\x34\x05\x67\x89\x0A\xBC\xDE\x0F\
		\x12\x34\x05\x67\x89\x0A\xBC\xDE\x0F"		# type string 

raw_data = 0x12340567890A

#truncated = 0xF & ord(var_c)

#print(ord(var_c), truncated)

# example 1 

print(hex(raw_data))

new_bytes = 0x0000000000
# move in first 2 bytes
new_bytes = (raw_data & 0xFFFF00000000) >> 8
# skip void nibble and put in data nibble that comes after 
new_bytes |= (raw_data & 0x00000F000000) >> 4 
new_bytes |= (raw_data & 0x000000FFFF00) >> 4
new_bytes |= (raw_data & 0x00000000000F)  

print(hex(new_bytes))

# EOF 
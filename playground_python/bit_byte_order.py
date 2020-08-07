#!/usr/bin/env python3 

'''
This script plays with bit and byte order when writing to a binary file. 

''' 



TIFF6_little_endian = 0x4949 	# ASCII 'II'
TIFF6_big_endian    = 0x4D4D 	# ASCII 'MM' 

TIFF6_magic_nr_little_endian = 0x2a00 	# ASCII '*'
TIFF6_magic_nr_big_endian    = 0x002a 	# ASCII '*' 


with open('bitbyte.DNF', "wb") as f: 
	# create header fields here (IFDs)
		
	f.write(TIFF6_big_endian.to_bytes(2, byteorder='big'))
	f.write(TIFF6_big_endian.to_bytes(2, byteorder='little'))

	f.write(TIFF6_magic_nr_big_endian.to_bytes(2, byteorder='big'))
	f.write(TIFF6_magic_nr_big_endian.to_bytes(2, byteorder='little'))

	f.write(TIFF6_magic_nr_little_endian.to_bytes(2, byteorder='big'))
	f.write(TIFF6_magic_nr_little_endian.to_bytes(2, byteorder='little'))





# EOF 
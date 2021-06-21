#!/usr/bin/env python3 

'''
src: https://www.youtube.com/watch?v=4zahvcJ9glg

https://www.bloggerdrive.com/understanding-and-implementing-rsa-algorithm-in-python/

https://stackoverflow.com/questions/3312364/implementing-rsa-in-python 

Diffie-Hellman key exchange
https://www.youtube.com/watch?v=M-0qt6tdHzk

PART 1: 

This is an example of the RSA algorithm. 
The algorithm is used to encrypt a message without need for prior exchange of a key. 

First, Alice sends Bob two (large, prime) numbers. 
Bob can use these numbers to encrypt a message and send it to Alice. 
Although anybody can have knowledge of Alice's numbers, only Alice can decrypt the message. 
'''

from math import gcd as bltin_gcd 


encryption_numbers = (5, 14)  # example number pairs: (5, 14), (159, 187), (1979, 2093)
decryption_numbers = (11, 14) # example number pairs: (11, 14), (159, 187), (3959, 2093). 
plain_message = '12' # value of plain message must be smaller than 2nd number in pair above 
#plain_message = ord('C')

# The following lines are identical. 
# However, pow() performs the operation more efficiently, according to python docs. 
# encrypted_message = int(plain_message) ** encryption_numbers[0] % encryption_numbers[1]
encrypted_message = pow(int(plain_message), encryption_numbers[0], encryption_numbers[1])

print('plain_message: ' + str(plain_message))
print('ciphertext: ' + str(encrypted_message))

decrypted_message = pow(int(encrypted_message), decryption_numbers[0], decryption_numbers[1])

print('decrypted message: ' + str(decrypted_message))

'''
PART 2: 

key generation 

1. pick 2 (very large) distinct prime numbers p, q
2. calculate the product of p, q = N (this is the 2nd encryption number that gets published!)
3. calculate the Phi function of N. The Phi-function calculates how many coprimes of N exist. 
   Coprimes are numbers that share no common factors with N. E.g. if N = 14, then all even numbers 
   and 7 are NOT coprime. 1, 3, 5, 9, 11 and 13 are. Those _6_ numbers are coprimes! 
   6 numbers exist that are coprimes of 14. 
   Fortunately, there is a formula (i.e., the phi function) to calculate Phi quickly: (p-1)(q-1)
4. Choose an encryption number e, that has two properties: 
   - it has to be between 1 and Phi(N): 1 < e < Phi(N)
   - must be coprime with N 
   - must be coprime with Phi(N)
   Inf N = 14, then only the numbers 3 and 5 remain. 3 is NOT coprime with Phi(N)=6. So only 5 remains! 
   We now have our two encryption numbers: e = 5, p*q = 14! 
5. Find decryption number d, that has properties: 
   - d*e mod Phi = 1, so in this case: d * 5 mod 6 = 1 
   - This means: pick a multiple of e for which mod 6 = 1 
   If we choose d = 11: 11*5 = 55. 55 mod 6 = 1. 
'''

# 1. 
p = 23 # 2, 23
q = 91 # 7, 91

# 2. 
N = p * q 
print('N = ' + str(N) + '. This will be the 2nd value used for encryption!')

# 3. 
Phi = (p - 1)*(q - 1)

# 4. 
coprimes = []
for x in range(1, Phi):
	# algorithm to calculate if x is coprime 
	# for gcd, see: 
	# https://stackoverflow.com/questions/39678984/efficiently-check-if-two-numbers-are-co-primes-relatively-primes
	# https://docs.python.org/3.7/library/math.html#math.gcd
	if (bltin_gcd(x, N) == 1) and (bltin_gcd(x, Phi) == 1):
		coprimes.append(x)

print('calculated coprimes of N, Phi: ' + str(coprimes))
e = coprimes[-1]
print('chosen as e: ' + str(e) + '. This will be the 1st value used for encryption!')

# 5. 
upper_boundary = N*10 # arbitrary chosen number 
d = []
for x in range(1, upper_boundary):
	# insert fancy algorithm here 
	if x * e % Phi == 1:
		d.append(x)

print('calculated values for d: ' + str(d))
print('All of these numbers can be used to decrypt the message, but I do not know if there is one to prefer')

# d = d[-1]
# print('chose for d: ' + str(d))

# EOF 


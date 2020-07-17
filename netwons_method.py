#!/usr/bin/python3 

# examples for how to solve an equation with Netwon's Method 

'''
Newton's Method: 
To solve an equation for a given variable, divide the equation by its derivative. 
Start at a random value and subtract the solution of f/f' from the random start 
value. 
With each iteration you approximate closer to the solution. 
In order for Newton's Method to work, you have to rearrange the equation so that 
you have 0 on one side of the equation (i.e. either '0 = rhs' or 'lhs = 0')

Newton's Method is only one algorithmic way to solve an equation. Other methods 
are e.g. Halley's Method and Householder's Method. 

Related(?): Finite Elements Method
'''

''' 
example 1: 

Solve for x:  x^2 - x = 42 

rearranged: 0 = x^2 - x -42

solutions: 7, -6 (with abc-formula)
'''

def approximate_ex_1(x):

	for i in xrange(0,10): 
		x -= (x*x - x - 42) / (2*x - 1)
		print(' iteration ' + str(i) +': x = ' + str(x))



approximate_ex_1(2.0) # random start value 

approximate_ex_1(-22.0) # let's try with a different start value 


'''
example 2: 

Solve for x: sqrt(10) = x 
rearranged: 10 = x^2 -> 0 = x^2 - 10 
'''

def approximate_ex_2(x):
	
	for i in xrange(0,10):
		x -= (x*x - 10) / (2*x)
		print(' iteration ' + str(i) +': x = ' + str(x))

approximate_ex_2(-1.0)
approximate_ex_2(1.0)
# EOF 
#!/usr/bin/env/python3   

# source: https://www.youtube.com/watch?v=BfS2H1y6tzQ&list=WL&index=38&t=94s 

# This code simulates a random walk on a grid where movement is possible in 4 
# possible directions: North, South, East, West. 
# Each random walk starts at the origin x=0, y=0. 


import random 

def random_walk(n):
	""" Return coordinates after n block random walks """
	x, y = 0, 0 

	for i in range(n):
		(dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
		x += dx 
		y += dy
	return (x, y)

number_of_walks = 20000 

for walk_length in range(1, 31):
	# number of walks 4 or fewer blocks from home 
	no_transport = 0 

	for i in range(number_of_walks):
		(x, y) = random_walk(walk_length) 
		distance = abs(x) + abs(y)
		if distance <= 4:
			no_transport += 1
	no_transport_percentage = float(no_transport) / number_of_walks
	print("Walk size = ", walk_length, 
		  " / % of no transport = ", 100*no_transport_percentage)

# EOF 
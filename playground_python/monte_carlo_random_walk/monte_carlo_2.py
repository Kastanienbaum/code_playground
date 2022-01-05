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

# let's do 25 random walks, each walk taking 10 steps
for i in range(25):
	walk = random_walk(10)
	print (walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))

# EOF 
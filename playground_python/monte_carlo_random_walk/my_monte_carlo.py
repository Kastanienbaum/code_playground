#!/usr/bin/env/python3 

# source: https://www.youtube.com/watch?v=BfS2H1y6tzQ&list=WL&index=38&t=94s 

# This code simulates a number n of random walks on a grid where movement is 
# possible in 4 directions: North, South, East, West. Each random walk starts 
# at the origin x=0, y=0 and has a fixed number of iterations (max_walk_length). 
# A threshold (no_transport_limit) can be set. This threshold defines a 
# 'radius' around the origin. If the random walk ends on average within this 
# radius, it is considered that the way back to the origin is walkable. 
# Otherwise, public transport needs to be used. 
#
#  +--+--+--+--+--+--+--+
#  |  |  |  |  |  |  |  |
#  +--+--+--+--+--+--+--+
#  |  |  |  |  |  |  |  |
#  +--+--+--+--+--+--+--+
#  |  |  |  |  |  |  |  |
#  +--+--+--+--+--+--+--+
#  |  |  |  |  |  |  |  |
#  +--+--+--+--+--+--+--+
#  |  |  |  |  |  |  |  |
#  +--+--+--+--+--+--+--+
#  |  |  |  |  |  |  |  |
#  +--+--+--+--+--+--+--+



import random 
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.ticker as ticker
# from matplotlib.ticker import MultipleLocator, FormatStrFormatter

def random_walk(n):
	""" Return coordinates after n block random walks """
	x, y = 0, 0 

	for i in range(n): 
		""" move in random direction: N,    S,       E,       W """
		(dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
		x += dx 
		y += dy
	return (x, y)


""" ----------------------- """
""" M A I N   P R O G R A M """
""" ----------------------- """

if __name__ == '__main__':

	# changeable parameters 
	number_of_walks = 100 
	max_walk_length = 31 
	no_transport_limit = 4 # threshold 

	data_list = list() # results for each walk length are stored here
	
	for walk_length in range(1, max_walk_length): 
		
		no_transport = 0 # number of walks 4 or fewer blocks from home 
	
		for i in range(number_of_walks):
			(x, y) = random_walk(walk_length) 
			distance_from_origin = abs(x) + abs(y)
			if distance_from_origin <= no_transport_limit:
				no_transport += 1
		no_transport_percentage = float(no_transport) / number_of_walks
		data_list.append(no_transport_percentage*100)
		print("Walk size = ", walk_length, " / % of no transport = ", 
			  100*no_transport_percentage)

	# print(data_list)
	# data_list = list(enumerate(data_list, 1))

	# plot results of random walks 
	plot_title = str(number_of_walks) + " random walks with a walk length of " \
			   + str(walk_length)

	x_axis = [] 
	for i in range(1, max_walk_length):
		x_axis.append(i)

	fig = plt.figure()

	gridspec = fig.add_gridspec(1,2)
	#fig, ax_lst = plt.subplots(1, 2)  # a figure with a 2x2 grid of Axes

	ax = plt.axes()
	ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
	ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
	#ax.yaxis.set_major_locator(ticker.MultipleLocator(5))


	plt.title(plot_title)
	plt.xlabel('walk length')
	plt.ylabel('% of walks <= 4 blocks away')

	plt.grid(b=None, which='major', axis='both')

	# calculate polynomial 
	z = np.polyfit(x_axis, data_list, 3) 
	f = np.poly1d(z)

	# calculate new x's and y's
	x_new = np.linspace(x_axis[0], x_axis[-1], 50)
	y_new = f(x_new)

	# plt.plot(x_axis, data_list, label='test')
	#plt.plot(x_axis, data_list, x_new, y_new, label='polynomial regression')
	plt.plot(x_axis, data_list, 'o', 
			  x_new, y_new, label='polynomial regression')

	plt.legend()
	plt.show()


# EOF 
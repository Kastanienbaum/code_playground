#!/usr/bin/python3 

# https://adventofcode.com/2020/day/3

'''with open('day3_input.txt', 'r') as f:

	# part 1, solution = 151

	# skip first line and get length of one chunk of forest
	chunklen = len(f.readline().strip('\n')) # 31

	# starting position in 2nd row 
	toboggan_pos = 3 
	encountered_trees = 0 

	for i, forest_row in enumerate(f):
		forest_row = forest_row.strip('\n')
		
		if (toboggan_pos >= chunklen): 
			shift = toboggan_pos % chunklen
			toboggan_pos = shift

		if forest_row[toboggan_pos] is '#':
			encountered_trees += 1

		toboggan_pos += 3'''

# part 2 (more general)

slopes = [(1,1) ,(3,1), (5,1), (7,1) ,(1,2)]
trees_list = []

with open('day3_input.txt', 'r') as f:
	chunklen = len(f.readline().strip('\n')) # 31

for slope in slopes:

	incr, down = slope

	with open('day3_input.txt', 'r') as f:

		encountered_trees = 0 
		toboggan_pos = incr

		f.readline()

		for i, forest_row in enumerate(f):
			if((i+1) % down == 0):
				forest_row = forest_row.strip('\n')

				if (toboggan_pos >= chunklen): 
					shift = toboggan_pos % chunklen
					toboggan_pos = shift

				if forest_row[toboggan_pos] is '#':
					encountered_trees += 1

				toboggan_pos += incr

		trees_list.append(encountered_trees)

print(trees_list)

prod = 1
for trees in trees_list:
	prod *= trees

print(prod)

# EOF 

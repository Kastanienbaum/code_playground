import re
import pandas as pd
import matplotlib.pyplot as plt 


file1="data1.txt"
file2="data2.txt"

indices = []
data = []
timestamps = []
voltages = []

# extracting data from first file
try:
	f=open(file1, 'r')

	for line in f:
		#extract index data points
		if "1st data: " in line:
			tmp = line.split("This is the 1st data: ")[1].strip()
			number = tmp.split("|")[0].strip()
			indices.append(int(number))
		#extract measured data points
		if "2nd data: " in line:
			tmp = line.split("2nd data: ")[1].strip()
			number = tmp.split(" ")[0].strip()
			data.append(float(number))
except Exception as e:
	print('error: ', e)
finally:
	f.close()

# extracting data from second file
try:
	f=open(file2, 'r')

	for line in f:
		#extract index data points
		if "The time is: " in line:
			tmp = line.split("The time is: ")[1].strip()
			timestamps.append(tmp)
		#extract measured data points
		if re.search(r'Value [0-9]:',line):
			tmp = line.split()
except Exception as e:
	print('error: ', e)
finally:
	f.close()

# create dataframe
zipped = list(zip(indices, data))
df = pd.DataFrame(zipped, columns=['INDICES','FLOATS'])

df.plot(x='INDICES', y='FLOATS')
plt.show()

#visualize data
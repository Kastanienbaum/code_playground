import re
import pandas as pd
import matplotlib.pyplot as plt 


file1="data1.txt"
file2="data2.txt"

indices = []
data = []
timestamps = []
voltage0 = []
voltage1 = []
voltage2 = []
voltage3 = []
voltage4 = []
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
		#if re.search(r'Value [0-9]:',line):
		if "Value 0: " in line:
			tmp = re.search("\d+\.\d+", line)
			voltage0.append(float(tmp.group(0)))
		if "Value 1: " in line:
			tmp = re.search("\d+\.\d+", line)
			voltage1.append(float(tmp.group(0)))
except Exception as e:
	print('error: ', e)
finally:
	f.close()

# create dataframe for 1st datafile
zipped = list(zip(indices, data))
df1 = pd.DataFrame(zipped, columns=['INDICES','FLOATS'])

df1.plot(x='INDICES', y='FLOATS')
plt.show()

# create dataframe for 2nd datafile
zipped = list(zip(timestamps, voltage0, voltage1))
df2 = pd.DataFrame(zipped, columns=['TIMESTAMPS','V0 [mV]','V1 [mV]'])

df2.plot(x='TIMESTAMPS', y='V0 [mV]')
plt.show()

#visualize data
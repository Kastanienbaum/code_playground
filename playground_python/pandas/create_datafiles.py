import random
import datetime
from datetime import timedelta


file1="data1.txt"
file2="data2.txt"

try:
	f = open(file1, 'w')
	for x in range(100):
		f.write('This is the 1st data: '+str(x)+ 
			' \t | This is 2nd data: ' + str(random.random()*100) + ' \t end\n')
except Exception as e:
	print('error: ', e)
finally:
	f.close()


try:
	f = open(file2, 'w')
	for x in range(100):
		f.write('The time is: '+
			str(datetime.datetime.now() + timedelta(minutes=x))+ '\n')
		for x in range(5):
			f.write('Value ' + str(x) + ': ' + str(random.random()*20-5) + 'mV\n')
except Exception as e:
	print('error: ', e)
finally:
	f.close()



print('END')

# EOF
#!/usr/local/bin/python3
# fibonacci 

import time 

def fib(limit):
	F0 = 0; 
	F1 = 1; 

	Fn_minus_2 = F0 
	Fn_minus_1 = F1

	start_time = time.time()
	start_perf_counter = time.perf_counter() # does include time elapsed during sleep and is system-wide
	start_process_time = time.process_time() # sum of system and user CPU time of the current process

	for x in range(0, limit):
		Fn = Fn_minus_2 + Fn_minus_1 
		Fn_minus_2 = Fn_minus_1 
		Fn_minus_1 = Fn 
		#yield(Fn)
		#if (x % 10000 == 0): 
		#	print(Fn); print()

	print("time: %f seconds" %(time.time() - start_time))
	print("perf_counter: %f seconds" %(time.perf_counter() - start_perf_counter))
	print("process_time: %f seconds" %(time.process_time() - start_process_time))

def main():

	while True:
		try:
			usr_input = int(input("How many fibonacci numbers shall be calculated?\n"))
			break
		except Exception as e:
			raise e

	print("I will now calculate the first %d fibonacci numbers" %usr_input)

	fib(usr_input)

if __name__ == '__main__':
	main()

# EOF 

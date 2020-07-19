// callback function example 

#include <stdint.h>
#include <stdio.h>

// caller function 
void print_calc_result(uint64_t (*calc_type)(uint64_t), uint64_t a)
{
	printf("result: %d\n", calc_type(a));
}

// callback 
uint64_t increment(uint64_t x) 
{
	return x+1; 
}

// callback 
uint64_t square(uint64_t x)
{
	return x*x; 
}


int main(void)
{
	uint64_t num = 42; 

	print_calc_result(&increment, num); 
	print_calc_result(&square, num); 

	return 0;
}
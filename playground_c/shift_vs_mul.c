#include <inttypes.h>
#include <stdio.h>
#include <time.h>
#include <limits.h>


void print_timediff (clock_t c0, clock_t c1) 
{
	printf("runtime: %f ms.\n", (c1 - c0) * 1000. / CLOCKS_PER_SEC);
}

int main(void)
{

	clock_t start; 
	clock_t stop;

	uint32_t a = 367001; 
	uint64_t b = 367001; 
	unsigned long loopsize = ULONG_MAX;

	printf("uint32_t\n");
	start = clock(); 
	for (unsigned long i = 0; i < loopsize; ++i) {
		a *= 2; 
		a /= 2; 
	}
	stop = clock(); 
	print_timediff(start, stop); 


	start = clock(); 
	for (unsigned long i = 0; i < loopsize; ++i) {
		a << 1; 
		a >> 1; 
	} 
	stop = clock(); 
	print_timediff(start, stop); 


	printf("uint64_t\n");
	start = clock(); 
	for (unsigned long i = 0; i < loopsize; ++i) {
		b *= 2; 
		b /= 2; 
	}
	stop = clock(); 
	print_timediff(start, stop); 

	start = clock(); 
	for (unsigned long i = 0; i < loopsize; ++i) {
		b << 1; 
		b >> 1; 
	}
	stop = clock(); 
	print_timediff(start, stop); 

	return 0;
}
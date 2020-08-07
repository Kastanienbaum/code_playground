#include <stdint.h>
#include <stdio.h>

int main()
{
	int a = 4294967293; 	 // 32 bit on this machine
	uint32_t b = 2147483648; // 32 bit on this machine
	int32_t c = 2147483648; // 32 bit on this machine
	short   s = 65535/2; 		// 16 bit on this machine 
	unsigned short us = 65535; 

	us = us + 42; 

	printf("%d\n", a);
	printf("%d\n", b);
	printf("%d\n", c);
	printf("%d\n", s);
	printf("%d\n", us);



	return 0;
}
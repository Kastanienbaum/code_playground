#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

int main(int argc, char const *argv[])
{
	uint16_t big_num = 0xBEEF; 
	uint8_t byte = 0x00; 

	printf("big_num = 0x%x\n", big_num);
	printf("byte = 0x%x\n", byte);

	byte = big_num; 

	printf("byte = %d\n", byte);

	return 0;
}
/*
inspired by https://cdecl.org/
*/

#include <stdio.h>

#define LEN 9

int main(int argc, char const *argv[])
{
	int arr[LEN] = {0,1,2,3,4,5, 6,7,8};

	int *p[3]; 

	p[3] = arr;

	for (int i = 0; i < LEN; ++i)
	{
		printf("%d\n", arr[i]);
	}

	printf("----------------\n");

	// use pointer arithmetic to access all elements of arr even though p can 
	// only contain 3 elements.
	for (int i = 0; i < 3; ++i)
	{
		printf("%d\n", *(p[3]+LEN-1-i));
	}

	return 0;
}
// function overloading 

#include <stdio.h>

void fancy_func() 
{
	printf("nothing passed here\n");
}

void fancy_func(int x) 
{
	printf("%d passed here\n", x);
}

void fancy_func(int x, int y) 
{
	printf("%d and %d passed here\n", x, y);
}


int main(void)
{
	int value = 123; 
	fancy_func(value); 
	fancy_func(); 
	fancy_func(0x86, value);

	return 0;
}
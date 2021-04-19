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

void fancy_func(float x)
{
  printf("%.15f passed here\n", x);
}


int main(void)
{
	int value = 123; 
  float fluffy = 3.1415; 
	fancy_func(value); 
	fancy_func(); 
	fancy_func(0x86, value);
  fancy_func(fluffy);

	return 0;
}
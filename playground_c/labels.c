// example for labels in C 

#include <stdio.h>

int main(void)
{
	int a = 1; 
	L1: 
		if (a == 111){printf("goodbye\n"); return 0;}
		a = 42; 
		printf("%d\n", a);

	L2: 
		a = 111; 
		printf("%d\n", a);
		goto L1;

	return 0;
}
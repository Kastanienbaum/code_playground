// reverse array indexing 

#include <stdio.h>

int main(void)
{
	int a[3] = {1,2,3}; 
	int len_a = sizeof(a) / sizeof(*a); 

	printf("This is what we normally see and expect \n");
	for (int i = 0; i < len_a; ++i)
	{
		printf("%d\n", a[i]);
	}

	printf("\nThis does the same \n");
	for (int i = 0; i < len_a; ++i)
	{
		printf("%d\n", i[a]);
	}

	printf("\nanother example with negative index\n");
	printf("%d, %d\n", -2[a], 0[a]);

	printf("\niterator starting with negativ value\n");
	for (int i = -len_a; i < len_a; ++i)
	{
		printf("%d\n", a[i]);
	}

	printf("\nand reversing the sign\n");
	for (int i = -len_a; i < len_a; ++i)
	{
		printf("%d\n", -i[a]);
	}

	return 0;
}

// EOF 
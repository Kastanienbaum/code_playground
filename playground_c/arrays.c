#include <stdlib.h>

void change (int **array, int length) 
{
	free(*array); 
	*array = malloc(length * sizeof(int)); 

	// on failure -> memory cannot be allocated 
	if (*array == NULL) { 
		return; 
	}
	for (int i = 0; i < length; ++i)
	{
		(*array)[i] = 1; 
	}
}

int main()
{
	int * array; 
	array = NULL; 

	change(&array, length); 

	free(array); 

	return 0;
}
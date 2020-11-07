/*
bubblesort algorithm  
*/

#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>

using namespace std; 

int main(int argc, char const *argv[])
{
	const int arraysize = 1024; 
	const int rand_upper_limit = RAND_MAX; // RAND_MAX

	int unsorted_array[arraysize]; 

	// use current time as seed for random generator
	srand((unsigned)time(NULL)); 

	for (int i = 0; i < arraysize; ++i) 
	{
		unsorted_array[i] = rand() % rand_upper_limit + 1; 
	}

	int *p1 = new int[arraysize]; 

	for (int i = 0; i < arraysize; ++i)
	{
		*(p1+i) = unsorted_array[i]; 
	}

	// for debugging 
	/*for (int i = 0; i < arraysize; ++i){cout << unsorted_array[i] << " ";}
	cout << endl; 
	for (int i = 0; i < arraysize; ++i){cout << *(p1+i) << " ";}
	cout << endl; */

	int *p2 = p1; 
	int sorted_pairs = -1; 
	int tmp = 0; 

	while (sorted_pairs != 0) 
	{
		sorted_pairs = 0;
		for (int i = 0; i < arraysize; ++i)
		{
			if (*(p1+i) > *(p2+i+1))
			{
				tmp = *(p1+i); 
				*(p1+i) = *(p2+i+1); 
				*(p2+i+1) = tmp; 
				++sorted_pairs;
			}
		}
	}

	cout << "sorted array: " << endl; 
	for (int i = 0; i < arraysize; ++i){cout << *(p1+i) << " ";}
	cout << endl; 

	delete p1; 
	delete p2; 

	return 0;
}


// EOF 


/*
Bubblesort: 
Compare two neighbouring elements. 
If the left element is larger than the right element, swap them. 
After proceeding with this comparison through the whole data structure, check if 
all elements are in order. 
*/

#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>

using namespace std; 


int main(int argc, char const *argv[])
{
	const int arraysize = 20; 
	const int rand_upper_limit = 99; // RAND_MAX

	int array[arraysize]; 

	// use current time as seed for random generator
	srand((unsigned)time(NULL)); 

	for (int i = 0; i < arraysize; ++i) {
		array[i] = rand() % rand_upper_limit + 1; 
	}

	cout << "unsorted array: " << endl; 
	for (int i = 0; i < arraysize; ++i){cout << array[i] << " ";}
	cout << endl; 


	int *nxt = array; 
	int sorted_pairs = -1; 
	int tmp = 0; 

	while (sorted_pairs != 0) 
	{
		sorted_pairs = 0;
		for (int i = 0; i < arraysize; ++i)
		{
			if (*(array+i) > *(nxt+i+1))
			{
				tmp = *(array+i); 
				*(array+i) = *(nxt+i+1); 
				*(nxt+i+1) = tmp; 
				++sorted_pairs;
			}
		}
	}

	cout << "sorted array: " << endl; 
	for (int i = 0; i < arraysize; ++i){cout << array[i] << " ";}
	cout << endl; 

	return 0;
}


// EOF 


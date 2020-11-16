/*
Heaposrt: 

*/

#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std; 


int main(int argc, char const *argv[])
{
	int size = 10;
	int upperLimit = 10;
	int array[size]; 

	// use current time as seed for random generator
	srand((unsigned)time(NULL));

	for (int i = 0; i < size; ++i) {
		array[i] = rand() % upperLimit + 1; 
	}
	
	for (int i = 0; i < size; ++i) {
		cout << array[i] << " "; 
	}
	cout << endl; 

	return 0;
}

// EOF 


/*
There are multiple ways of initializing variables in C++. 

*/

#include <iostream>
#include <string>

using namespace std; 

int main(int argc, char const *argv[])
{
	int a = 12; 
	int b {a % 2 ? 1 : 2}; 
	cout << "a: " << a << " b: " << b << endl; 

	char c ('x'); 
	char d {'y'}; 
	char *p (&c); 
	cout << "c: " << c << " d: " << d << " p: " << *p << endl; 

	string hel {"hello"}; 
	string wor = "world"; 
	cout << hel + " " << wor << endl; 

	return 0;
}
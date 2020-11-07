/*
Linked List in C++
*/

#include <iostream>

using namespace std; 

class LinkedList
{
	// members declared before the first access specifier are automatically private 
	int item; 
	LinkedList* next_element; 
	LinkedList* previous_element;

	public:		
		LinkedList(int a){
			*next_element = NULL; 
			*previous_element = NULL; 
			item = a; 
		}
		//~LinkedList();

		void addElement() {
			cout << "addElement" << endl; 
		} 

		void deleteElement() {
			cout << "deleteElement" << endl; 
		}


	
} linkedList;


int main(int argc, char const *argv[])
{
	LinkedList list_1(3); 


	return 0;
}


// EOF 


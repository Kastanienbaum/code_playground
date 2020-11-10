/*
Linked List in C++

https://www.youtube.com/watch?v=vcQIFT79_50
https://www.learn-cpp.org/en/Linked_lists

*/

#include <iostream>

using namespace std; 

struct Node
{
	int item; 
	struct Node* next; 
} node;

class MyLinkedList
{
	// members declared before the first access specifier are automatically private 
	Node *head; 

	public:	
		MyLinkedList(int);
		void addElement(int); 
}; 

MyLinkedList::MyLinkedList(int a){
	head = nullptr; 
}

void MyLinkedList::addElement(int newElem) {
	node *tmp = new Node; 
	cout << "addElement" << endl; 
} 


int main(int argc, char const *argv[])
{
	return 0;
}


// EOF 


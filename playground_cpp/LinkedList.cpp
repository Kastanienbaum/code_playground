/*
Linked List in C++

https://www.youtube.com/watch?v=vcQIFT79_50
https://www.learn-cpp.org/en/Linked_lists

TODO 
- add destructor? 
- search for memory leaks 

*/

#include <iostream>

using namespace std; 

typedef struct _Node
{
	int item; 
	struct _Node* pNext; 
} Node;

class ClassNode
{
	int item; 
	ClassNode *pNext; 
public:
	ClassNode();
	~ClassNode();
	
};

class MyLinkedList
{
	// members declared before the first access specifier are automatically 
	// private 
	Node* pHead; 
	Node* pTail; 

	public:	
		MyLinkedList();

		void addNodeAtEnd(int); 
		void deleteNodeAtEnd(); 
		void printList(); 
}; 

MyLinkedList::MyLinkedList(){
	// initialize list pointers
	pHead = nullptr; 
	pTail = nullptr; 
}


void MyLinkedList::addNodeAtEnd(int newElem) {
	// allocate memory for new node in list and initialize node members. 
	Node *pNew = new Node; 
	pNew->item = newElem; 
	pNew->pNext = nullptr; 

	// add node at the end of the list
	if (pHead == nullptr)
	{
		pHead = pNew; 
		pTail = pNew; 
	}
	else {
		// let current tail node point to new node
		pTail->pNext = pNew; 
		// update tail and let it point to new node as well, since new node is 
		// the new tail!  
		pTail = pNew; 
	}
} 

void MyLinkedList::deleteNodeAtEnd() {

}


void MyLinkedList::printList() {
	if (pHead == nullptr) {cout << "List is empty" << endl;}
	else 
	{
		Node* pNow = pHead; 
		while(pNow != nullptr) {
			cout << pNow->item << " "; 
			pNow = pNow->pNext;
		}
		cout << endl; 
	}
}


int main(int argc, char const *argv[])
{
	MyLinkedList list1; 

	for (int i = 0; i < 10; ++i)
	{
		list1.addNodeAtEnd(i); 
	}
	list1.printList(); 

	return 0;
}


// EOF 


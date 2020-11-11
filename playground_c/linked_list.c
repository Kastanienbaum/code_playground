/*
This is an implementation of a linked list in C. 
It shall demonstrate how a linked list works and is mainly a programming 
exercise for me. 

TODO: 
- add return value checks (mainly malloc())

*/

#include <stdio.h>
#include <stdlib.h>

#ifdef _WIN32 || WIN32
	#include <windows.h>
#endif 

typedef struct Node_
{
	int item; 
	struct Node_ *pNext; 
} Node; 


Node* createList (int val) {
	Node* pHead = (Node*)malloc(sizeof(Node)); 
	pHead->item = val; 
	pHead->pNext = NULL; 
	return pHead; 
}

void addNodeAtEndOfList (Node* node, int val) {
	// traverse list until the last list element is reached 
	while(node->pNext != NULL) {node = node->pNext;}
	
	// allocate memory for new list element 
	// and add it at the end of the current list
	Node* pNew = (Node*)malloc(sizeof(Node)); 
	node->pNext = pNew; 
	pNew->pNext = NULL; 
	pNew->item = val; 
}

void deleteNodeAtEndOfList (Node* node) {
	Node* pNewTail = NULL; 
	// traverse list until the last list element is reached 
	while (node->pNext != NULL) {
		pNewTail = node; 
		node = node->pNext;
	} 
	free(node); 
	// let the new last element point to NULL
	pNewTail->pNext = NULL; 
}


void printList (Node* listElem) {
	Node *pNow = listElem; 
	while (pNow != NULL) {
		printf("%d ", pNow->item);
		pNow = pNow->pNext; 
	}  
	printf("\nEND OF LIST\n");
}


int main(int argc, char const *argv[])
{
	Node *my_list = createList(0); 
	for (int i = 1; i < 10; ++i) {
		addNodeAtEndOfList(my_list, i); 
	}
	printList(my_list);

	for (int i = 0; i < 3; ++i) {
		deleteNodeAtEndOfList(my_list); 
	}
	printList(my_list); 	

	return 0;
}
// EOF 


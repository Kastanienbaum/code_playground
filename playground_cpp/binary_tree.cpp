/*
Binary Tree 
*/

#include <iostream>

using namespace std; 

typedef struct Node_
{
	int val; 
	struct Node_ *left; 
	struct Node_ *right; 

} Node;


class BinaryTree
{
	unsigned int height; 
	Node* root; 

public:
	BinaryTree();
	void addNode(int); 
	//printTree(); 
	//getMaxPossibleNumberOfNodes(); 
	//~BinaryTree();
	
};

BinaryTree::BinaryTree() {
	root = nullptr; 
	height = 1; 
}

void BinaryTree::addNode(int v) {
	Node* n = new Node; 
	n->val = v; 
	n->left  = nullptr; 
	n->right = nullptr; 

	if (root == nullptr) {root = n; return;}

	Node* now = root; 
	while(1) {
		if (now == nullptr){now = n;}
		else 
			if (now->left != nullptr && now->right != nullptr){now = now->left;}
		else 
			if (now->left != nullptr && now->right == nullptr){now->left = n;}
		//else
	}

}

int main(int argc, char const *argv[])
{
	BinaryTree bin;
	

	return 0;
}

// EOF 

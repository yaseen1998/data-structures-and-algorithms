# Trees
<!-- Short summary or background information -->
A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have only 2 children, we typically name them the left and right child.
## Challenge
<!-- Description of the challenge -->
it must create 3 class .binary tree , node , binary search tree .
A Binary Tree node contains following parts.

Data
Pointer to left child
Pointer to right child
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O :
binary tree :
time complexity : O(log n)O(logn) time where n is the number of nodes in the tree.
space complexity : O(n) in both the average and the worst cases.
## API
<!-- Description of each method publicly available in each of your trees -->
class Node : it contain left and right and value for each data
class binary tree :
method one : preorder_print it arrange data from root->left->right
method two : inorder_print it arrange data from left->root->right
method three : postorder_print it arrange data from left->right->root
method four : print_tree it print data

class BST:(binary search tree) :
method one add : it add new data in tree and arrange it
method two contains : it check if tree includes the specific number or not

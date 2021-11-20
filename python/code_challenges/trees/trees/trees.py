class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right =None
class BinaryTree:
    def __init__(self,root=None):
        self.root = Node(root)
    def print_tree(self,traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(self.root,'')
        if traversal_type == 'inorder':
            return self.inorder_print(self.root,'')
        if traversal_type == 'postorder':
            return self.postorder_print(self.root,'')
        else:
            print(f'traversal type {traversal_type} is not support ')
            return 'its empty or this traversal_type is not support'
    def preorder_print(self,start,traversal):
        """root->left->right"""
        if start:
            traversal+=str(start.value)+'-'
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal
    def inorder_print(self,start,traversal):
        """left->root->right"""
        if start:
            traversal = self.inorder_print(start.left,traversal)
            traversal+=str(start.value)+'-'
            traversal = self.inorder_print(start.right,traversal)
        return traversal
    def postorder_print(self,start,traversal):
        """left->right->root"""
        if start:
            traversal = self.postorder_print(start.left,traversal)
            traversal = self.postorder_print(start.right,traversal)
            traversal+=str(start.value)+'-'
        return traversal
class BST:
    def __init__(self,root):
        self.root = Node(root)

    def add(self,data,current=None):
        if self.root is None :
            self.root =Node(data)
        else:
            self._insert(data,self.root)
    def _insert(self,data,current):
        if current.value>data:
            if current.left:
                self._insert(data,current.left)
            else:
                current.left = Node(data)
        if current.value<data:
            if current.right:
                self._insert(data,self.root.right)
            else:
                current.right = Node(data)
        elif current.value==data:
            print(f'there is value is repeated')
    def contains(self, value):
        if not self.root:
            return "This is empty tree"

        current_node = self.root

        while current_node:

            if current_node.value == value:
                return True

            if current_node.value < value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return False


    def print_BST(self):
        if self.root != None:
            return self._print(self.root,'')

    def _print(self,start,traversal):
        """left->root->right"""
        if start:
            traversal = self._print(start.left,traversal)
            traversal+=str(start.value)+'-'
            traversal = self._print(start.right,traversal)
        return traversal


# tree = BinaryTree(1)
# tree.root.left=Node(2)
# tree.root.right = Node(3)
# tree.root.left.left =Node(4)
# tree.root.left.right =Node(5)
# tree.root.right.left =Node(6)
# tree.root.right.right =Node(7)
# tree.root.right.right.right =Node(8)
# print(tree.print_tree('preorder'))
# # print(tree.print_tree('inorder'))
# # print(tree.print_tree('postorder'))
root = BST(10)
list1 = [20,4,30,1,8,5,6]
for i in list1:
    (root.add(i))
root.add(20)
# print(root.print_BST())

# print(root.contains(11))

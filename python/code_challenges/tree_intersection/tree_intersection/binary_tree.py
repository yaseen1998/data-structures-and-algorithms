class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right =None

class Binary_tree:
    def __init__(self,root):
        self.node = Node(root)
        self.size = 1
        self.result = set()
    def add(self,data):
        self._insert(data,self.node)

    def _insert(self,data,current):
        if current.value>data:
            if current.left:
                self._insert(data,current.left)
            else:
                current.left = Node(data)
                self.size+=1
        if current.value<data:
            if current.right:
                self._insert(data,current.right)
            else:
                current.right = Node(data)
                self.size+=1
        elif current.value==data:
            return
    def print_BST(self):
        if self.node != None:
            return self._print(self.node,'')

    def _print(self,start,traversal):
        """left->root->right"""
        if start:
            traversal = self._print(start.left,traversal)
            self.result.add(start.value)
            traversal = self._print(start.right,traversal)
        return self.result

# ll= Binary_tree(20)
# ll.add(40)
# ll.add(10)
# ll.add(15)
# ll.add(30)
# ll.add(3)
# print(ll.print_BST())



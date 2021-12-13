from binary_tree import Binary_tree
from linkedlist import LinkedList

tree1 = Binary_tree(20)
tree1.add(40)
tree1.add(10)
tree1.add(15)
tree1.add(30)
result1 = tree1.print_BST()

tree2 = Binary_tree(20)
tree2.add(4)
tree2.add(19)
tree2.add(45)
tree2.add(30)
result2 = tree2.print_BST()

class Intersection:
    def __init__(self,tree1,tree2):
        self.tree1 = tree1
        self.tree2 = tree2
        self.size1 = 1024
        self.map1 = [None]*1024
        # self.map2 = [None]*1024
        self.add()
    def hash(self,value):
        sum_asci = 0
        value = str(value)
        for char in value:
            asci_chr = ord(char)
            sum_asci += asci_chr
        temp_value = sum_asci *19
        hash_key = temp_value % self.size1
        return hash_key

    def add(self):
        for i in self.tree1:
            hash_key = self.hash(i)
            self.map1[hash_key]= i

hash = Intersection(result1,result2)
for index,item in enumerate (hash.map1):
    if item:
        print(index , item)

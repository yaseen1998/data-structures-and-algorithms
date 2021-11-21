class Node:
    def __init__(self, data=None):
        self.value = data
        self.left = self.right = None

def findMax(root):

    # Base case
    if (root == None):
        return -999999
    if (root.value == None):
       return 'the tree is empty'

    # Return maximum of 3 values:
    # 1) Root's data 2) Max in Left Subtree
    # 3) Max in right subtree
    res = root.value
    lres = findMax(root.left)
    rres = findMax(root.right)
    if (lres > res):
        res = lres
    if (rres > res):
        res = rres
    return res

def max(root):
    result = findMax(root)
    if findMax==-999999:
        return 'the tree is empty'
    return result

# tree = Node()
# print(tree)

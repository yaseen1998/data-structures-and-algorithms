# Python program to print level
# order traversal using Queue

# A node structure


class Node:
    # A utility function to create a new node
    def __init__(self, key=None):
        self.data = key
        self.left = None
        self.right = None

# Iterative Method to print the
# height of a binary tree


def printLevelOrder(root):
    # Base Case
    if root.data is None:
        return 'empty'

    # Create an empty queue
    # for level order traversal
    queue = []
    stri=''
    # Enqueue Root and initialize height
    queue.append(root)
    while(len(queue) > 0):

        # Print front of queue and
        # remove it from queue
        stri+=str((queue[0].data))+'-'
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)
            print('left',node.left.data)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)
    return stri

# Driver Program to test above function


root = Node()
print(printLevelOrder(root))

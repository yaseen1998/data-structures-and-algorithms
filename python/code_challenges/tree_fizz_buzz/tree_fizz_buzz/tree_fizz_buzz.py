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


def fizz_buzz(root):
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
        if (queue[0].data)%5==0 and (queue[0].data)%3==0:
            queue[0].data='FizzBuzz'
        elif (queue[0].data)%5==0:
            queue[0].data='Buzz'
        elif (queue[0].data)%3==0:
            queue[0].data='Fizz'


        # Print front of queue and
        # remove it from queue
        stri+=str((queue[0].data))+'-'
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)
    return stri

# Driver Program to test above function


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)
root.left.right = Node(9)
print(fizz_buzz(root))

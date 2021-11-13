
# from stack_and_queue.node import Node
class Node():
   def __init__(self, dataval=None):
    self.dataval = dataval
    self.nextval = None

class Stack:

    def __init__(self):
        self.topval = None

    def push(self, value):
        if self.topval is None:
            self.topval = Node(value)
        else:
            new_node = Node(value)
            new_node.nextval = self.topval
            self.topval = new_node

    def pop(self):
        if self.topval is None:
            return None
        else:
            popped = self.topval.dataval
            self.topval = self.topval.nextval
            return popped

    def peek(self):
        if self.topval :
            return self.topval.dataval
        else:
            return "Stack is Empty"


    def isEmpty(self):
        if self.topval == None:
            return False
        else:
            return True

if __name__ == "__main__":
    stack = Stack()

    stack.push(4)
    stack.push(1)
    stack.push(2)
    stack.push(25)
    stack.pop()


    print(stack.peek())

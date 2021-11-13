# from stack_and_queue.node import Node
class Node():
   def __init__(self, dataval=None):
    self.dataval = dataval
    self.nextval = None

class Queue():
    def __init__(self):
        self.front = None ; self.rear = None

    def EnQueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.nextval = temp
        self.rear = temp

    def DeQueue(self):

        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.nextval

        if(self.front == None):
            self.rear = None

    def peek(self):
        if self.front :
            return self.front.dataval
        else:
            return "queue is Empty"
    def isEmpty(self):
        if self.front == None and self.rear == None:
             return True
        else:
            return False


if __name__ == "__main__":
    queue = Queue()

    queue.EnQueue(5)
    queue.EnQueue(9)
    queue.DeQueue()

    print(queue.peek())

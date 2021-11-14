from stack_and_queue.stack import Stack
class Pseudo_Queue:
    def __init__(self,stack):
        self.stack2 = Stack()
        self.stack1=stack


    def enqueue(self, value):
        result=''
        self.stack1.push(value)


        while self.stack1.topval.nextval:
                result+=f'[{self.stack1.peek()}]->'
                self.stack1.topval = self.stack1.topval.nextval
        result+=f'[{self.stack1.peek()}]'
        return result

    def dequeue(self):
        while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        removedValue=self.stack2.pop()

        return removedValue




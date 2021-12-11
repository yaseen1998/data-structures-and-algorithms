
class Node:
    def __init__(self,value):
        self.value =value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add (self,value):
        new_node = Node(value)
        if not self.head :
            self.head = new_node
        else :
            current = self.head
            while current.next:
                current=current.next
            current.next = new_node




    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return f'{result}'


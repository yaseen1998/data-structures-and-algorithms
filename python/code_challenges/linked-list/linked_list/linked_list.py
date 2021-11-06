class LinkedList:
    def __init__(self):
        self.head = None

    def insert (self,value):
        # 1 & 2: Allocate the Node &
    #        Put in the data
      new_node = Node(value)

    # 3. Make next of new Node as head
      new_node.next = self.head

    # 4. Move the head to point to new Node
      self.head = new_node

    def includes(self,value):
        if self.head  is not None :
            current =self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False


    def to_string(self):
        if self.head:
            data_str = ''
            current = self.head
            while current:
                data_str += '{'+str(current.value)+'}-> '
                current = current.next
            data_str += 'NULL'
            return data_str




class Node:
    def __init__(self,value):
        self.value =value
        self.next = None

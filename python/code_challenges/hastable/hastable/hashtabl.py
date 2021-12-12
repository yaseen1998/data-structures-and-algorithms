from .linkedlist import LinkedList

class Hashtable:
    def __init__(self,size):
        self.size = size
        self.map =[None]*size
    def hash(self,key):
        sum_asci = 0
        for char in key:
            asci_chr = ord(char)
            sum_asci += asci_chr
        temp_value = sum_asci *19
        hash_key = temp_value % self.size
        return hash_key

    def add(self,key,value):
        hash_key = self.hash(key)
        if not self.map[hash_key]:
            self.map[hash_key] = LinkedList()
        self.map[hash_key].add((key,value))

    def get(self,key):
        hash_key = self.hash(key)
        if self.map[hash_key]:
            current = self.map[hash_key].head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next

        return 'this element does not exist'

    def contains(self, key):
        hash_key = self.hash(key)
        if self.map[hash_key]:
            current = self.map[hash_key].head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
        else:
            return False


if __name__ == '__main__':
    hash = Hashtable(1024)
    hash.add("AHMAD",30)
    hash.add("YAHYA",'how are')
    hash.add("HAMAD",55)
    print(hash.get('HAMAD'))
    # print(hash.contains('slent'))
    # for index,item in enumerate (hash.map):
    #     if item:
    #         print(index , item)
    print(hash.map[hash.hash('AHMAD')].__str__())

class Node : 
    def __init__(self,value):
        self.value = value

class Edge:
    def __init__(self,second_node,weight=0):
        self.second_node = second_node
        self.weight = weight

class Graph : 
    def __init__(self):
        self.__adj__list = {}
    
    def add_node(self,value):
        node = Node(value)
        self.__adj__list[node.value] = []
        return node
    
    def add_edge(self,first_node,second_node = None,weight = 0):
        if first_node.value not in self.__adj__list or second_node.value not in self.__adj__list :
            raise KeyError('node is not exist')

        edge = Edge(second_node.value,weight)

        self.__adj__list[first_node.value].append([edge.second_node,edge.weight])
    def business_trip(self , arr):
        result = 0
        lenght = len(arr)
        answer = True
        while len(arr)-1:
        
            start_node = arr[0]
            next_node = arr[1]
            if start_node not in self.__adj__list:
                raise KeyError('node is not exist')
            for data in self.__adj__list[start_node]:
                if next_node in data:
                    result +=(data[1])
                    answer = True
                    break
                else:
                    answer = False
            arr.pop(0)
        return answer,f'${result}'
            
        

    
# r = Graph()
# node1 = r.add_node('amman')
# node2 = r.add_node('zarqa')
# node3 = r.add_node('jarash')
# (r.add_edge(node1,node2,80))
# (r.add_edge(node2,node3,30))
# print(r.business_trip(['amman','zarqah','jarash']))

# graph = Graph()
# node1=graph.add_node('amman')
# node2=graph.add_node('zarqa')
# node3=graph.add_node('aqabe')
# node4=graph.add_node('jarash')
# node5=graph.add_node('ajloon')
# node6=graph.add_node('maan')
# graph.add_edge(node1,node2,30)
# graph.add_edge(node1,node4,20)
# graph.add_edge(node4,node5,10)
# graph.add_edge(node1,node6,40)
# graph.add_edge(node6,node3,25)
# print(graph.business_trip(['amman','zarqa']))

test = {'amman':{'zarqa':20,'maan': 25} }
print(test['amman']['zarqa'])
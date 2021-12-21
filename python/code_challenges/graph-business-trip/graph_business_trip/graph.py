from queue import Queue
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
            
    def breadth_first(self,node):

       breadth=Queue()
       brunch=[]
       nodes=[]
       breadth.enqueue(node)
       brunch.append(node)
       while breadth.front:
            front=breadth.dequeue()
            nodes.append(front.value)
            for data in self.adjacency_list[front]:
                if data.node not in brunch:
                   brunch.append(data.node)
                   breadth.enqueue(data.node)
       return nodes

def graph_depth_first(graph,node):

    data= []
    stack = [node]
    while(len(stack)!= 0):
        s = stack.pop()
        if s not in data:
            data.append(s)
        if s not in graph:
            continue
        for neighbor in graph[s]:
            stack.append(neighbor)

    return" ".join(data)   

if __name__=="__main__":
    g=Graph()
    a=g.add_node('a')
    b=g.add_node('b')
    c=g.add_node('c')

    g.add_edge(a,b,5)
    g.add_edge(b,c,4)  
    g.add_edge(c,a,3)
    g.add_edge(b,a,1)


    graph = {"A":["B","C", "D"],
           "B":["E"],
           "C":["F","G"],
           "D":["H"],
           "E":["I"],
           "F":["J"]}
    
    DFS =graph_depth_first(graph, "A")

    print(DFS)
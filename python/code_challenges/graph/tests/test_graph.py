
from graph import __version__
from graph.graph import Graph
import pytest
def test_version():
    assert __version__ == '0.1.0'

# Node can be successfully added to the graph
def test_add_get_nodes(graph):
    Graph,test = graph
    expected = Graph.get_nodes()
    actual = [1,2,3,4,5,6]
    assert expected == actual

def test_neighbors(graph):
    Graph,node1 = graph
    expected =  Graph.get_neighbors(node1)
    actual =  [[2, 0], [3, 0], [4, 0]]
    assert expected == actual

def test_add_node():
    graph = Graph()
    graph.add_node(5)
    actual = graph.get_graph()
    expected = {5: []}
    assert actual == expected


# An edge can be successfully added to the graph
def test_add_edge(graph):
    Graph,node1 = graph
    actual =  Graph.get_graph()
    expected =  {1: [[2, 0], [3, 0], [4, 0]], 2: [], 3: [[5, 0], [6, 0]], 4: [[5, 0]], 5: [], 6: []}
    assert actual == expected


# The proper size is returned, representing the number of nodes in the graph
def test_get_size(graph):
    Graph,Node1 = graph
    actual = Graph.size()
    expected = 6
    assert actual == expected

# # A graph with only one node and edge can be properly returned
def test_add_one_node():
    graph = Graph()
    graph.add_node(10)
    actual = graph.get_graph()
    expected = {10:[]} 
    assert actual == expected

# # An empty graph properly returns null
def test_empty_graph():
    graph = Graph()
    actual = graph.size()
    expected = 'null'
    assert actual == expected

@pytest.fixture
def graph():
    graph = Graph()
    node1=graph.add_node(1)
    node2=graph.add_node(2)
    node3=graph.add_node(3)
    node4=graph.add_node(4)
    node5=graph.add_node(5)
    node6=graph.add_node(6)
    # node1 : node2,3,4
    graph.add_edge(node1, node2)
    graph.add_edge(node1, node3)
    graph.add_edge(node1, node4)

    # node3: node5,6
    graph.add_edge(node3, node5)
    graph.add_edge(node3, node6)

    # node4 : node6
    graph.add_edge(node4, node5)

    return graph,node1
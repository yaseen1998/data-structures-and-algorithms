from graph_business_trip import __version__
from graph_business_trip.graph import Graph,graph_depth_first
import pytest

# def test_version():
#     assert __version__ == '0.1.0'

def test_one_graph(graph):
    expected = graph.business_trip(['amman','zarqa'])
    actual = (True, '$30')
    assert actual==expected

def test_multi_graph(graph):
    expected = graph.business_trip(['amman','maan','aqabe'])
    actual = (True, '$65')
    assert actual==expected

def test_one_graph_false(graph):
    expected = graph.business_trip(['amman','aqabe'])
    actual = (False, '$0')
    assert actual==expected

def test_multi_graph_false(graph):
    expected = graph.business_trip(['amman','jarash','aqabe'])
    actual = (False, '$20')
    assert actual==expected
    
def test_breadth():
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
    
    expected =graph_depth_first(graph, "A")
    actual = 'A D H C G F J B E I'
    assert actual == expected


@pytest.fixture
def graph():
    graph = Graph()
    node1=graph.add_node('amman')
    node2=graph.add_node('zarqa')
    node3=graph.add_node('aqabe')
    node4=graph.add_node('jarash')
    node5=graph.add_node('ajloon')
    node6=graph.add_node('maan')
    graph.add_edge(node1,node2,30)
    graph.add_edge(node1,node4,20)
    graph.add_edge(node4,node5,10)
    graph.add_edge(node1,node6,40)
    graph.add_edge(node6,node3,25)
    return graph

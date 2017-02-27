__author__ = 'Ryan Donovan'

import unittest
from graph import Graph
from graph_functions import is_complete
from graph_functions import nodes_by_degree

class TestGraphMethods(unittest.TestCase):

# Test get_adjlist() with existing node in graph that doesn't have any values in its adjacency list
    def test_get_adjlist_G2(self):
        dict = {'A': []}
        g1 = Graph(dict)
        test = g1.get_adjlist('A')
        self.assertEqual(test,[])

#Test is_adjacent when node2 is not in the graph
    def test_is_adjacent_G3(self):
        dict = {'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : []}
        g = Graph(dict)
        test = g.is_adjacent('A', 'F')
        self.assertFalse(test)

#Test num_nodes() when there are zero nodes in the graph
    def test_num_nodes_G4(self):
        dict = {}
        g1 = Graph(dict)
        test = g1.num_nodes()
        self.assertEqual(test,0)

#Test num_nodes() when there are nodes in the graph
    def test_num_nodes_G5(self):
        dict = { 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] }
        g1 = Graph(dict)
        test = g1.num_nodes()
        self.assertEqual(test,len(dict.keys()))

#Test contains when there are zero nodes in the graph
    def test_contains_G6(self):
        dict = {}
        g1 = Graph(dict)
        test = g1.__contains__('A')
        self.assertFalse(test)

#Test add_node when the node is not already in the graph
    def test_add_node_G7(self):
        dict = { 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] }
        g1 = Graph(dict)
        test = g1.add_node('F')
        self.assertTrue(test)
        assert g1.__contains__('F')

#Test add_node when the node is already in the graph
    def test_add_node_G8(self):
        dict = {'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []}
        g1 = Graph(dict)
        test = g1.add_node('B')
        self.assertFalse(test);

#test link_nodes when they are already adjacent to each other
    def test_link_nodes_G9(self):
        dict = {'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []}
        g1 = Graph(dict)
        test = g1.link_nodes('A','B')
        self.assertFalse(test)

# test link_nodes when they are not already adjacent to each other
    def test_link_nodes_G10(self):
        dict = {'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []}
        g1 = Graph(dict)
        test = g1.link_nodes('A', 'E')
        self.assertTrue(test)
        self.assertTrue(g1.dict['A'].__contains__('E'))
        self.assertTrue(g1.dict['E'].__contains__('A'))

#test unlink_nodes when they are not already linked
    def test_unlink_nodes_G11(self):
        dict = {'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []}
        g1 = Graph(dict)
        test = g1.unlink_nodes('A','E')
        self.assertFalse(test);

#test unlink_nodes when they are linked
    def test_unlink_nodes_G12(self):
        dict = {'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []}
        g1 = Graph(dict)
        test = g1.unlink_nodes('A', 'B')
        self.assertTrue(test)
        self.assertFalse(g1.dict['A'].__contains__('B'))
        self.assertFalse(g1.dict['B'].__contains__('A'))

#test del_node when the node is both in the graph and in the adjacency lists of other nodes
    def test_del_node_G13(self):
        dict = {'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []}
        g1 = Graph(dict)
        test = g1.del_node('A')
        self.assertTrue(test)
        self.assertFalse(g1.dict.keys().__contains__('A'))
        for k in g1.dict.keys():
           self.assertFalse(g1.dict[k].__contains__('A'))

#test del_node when the node is not in the graph
    def test_del_node_G14(self):
        dict = {'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []}
        g1 = Graph(dict)
        test = g1.del_node('F')
        self.assertFalse(test)

#test len
    def test_len_G15(self):
        dict = {'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []}
        g1 = Graph(dict)
        test = g1.__len__()
        self.assertEqual(test, len(dict.keys()))

#Test is_adjacent when node2 is in the graph and adjacent to node1
    def test_is_adjacent_G16(self):
        dict = {'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []}
        g = Graph(dict)
        test = g.is_adjacent('A', 'B')
        self.assertTrue(test)

#Test is_adjacent when node2 is in the graph and not adjacent to node1
    def test_is_adjacent_G17(self):
        dict = {'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []}
        g = Graph(dict)
        test = g.is_adjacent('A', 'C')
        self.assertFalse(test)

#Test get_adjlist() with existing node in graph that has valid adj list
    def test_get_adjlist_G18(self):
        dict = {'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []}
        g1 = Graph(dict)
        test = g1.get_adjlist('A')
        self.assertEqual(test,['B', 'D'])

#test link_nodes when they are the same node
    def test_link_nodes_G19(self):
        dict = {'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []}
        g1 = Graph(dict)
        test = g1.link_nodes('A', 'A')
        self.assertFalse(test)
#test unlink_nodes when they are the same node
    def test_link_nodes_G20(self):
        dict = {'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []}
        g1 = Graph(dict)
        test = g1.unlink_nodes('A', 'A')
        self.assertFalse(test)

# *************** TEST GRAPH FUNCTIONS *************************

    def test_is_complete(self):
        test = is_complete("hello")
        self.assertRaises(TypeError)


    def test_is_complete(self):
        dict = {'A': ['B', 'D']}
        g1 = Graph(dict)
        test = is_complete(g1)
        self.assertTrue(test)

    def test_is_complete(self):
        dict = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['B','A']}
        g1 = Graph(dict)
        test = is_complete(g1)
        self.assertTrue(test)

    def test_nodes_by_degree(self):
        test = is_complete("hello")
        self.assertRaises(TypeError)

    def test_nodes_by_degree(self):
        dict = {'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': []}
        g1 = Graph(dict)
        test = nodes_by_degree(g1)
        self.assertEqual(test, [['B', 3], ['A', 2], ['C', 1], ['D', 0]])

if __name__ == '__main__':
        unittest.main()


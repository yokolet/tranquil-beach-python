import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.undirected_graph_node import UndirectedGraphNode

class TestUndirectedGraphNode(unittest.TestCase):
    def setUp(self):
        self.builder = UndirectedGraphNode

    def test_1(self):
        g = {
            "$id":"1",
            "neighbors":[
                {
                    "$id":"2",
                    "neighbors":[
                        {
                            "$ref":"1"
                        },{
                            "$id":"3",
                            "neighbors":[
                                {
                                    "$ref":"2"
                                },{
                                    "$id":"4",
                                    "neighbors":[
                                        {
                                            "$ref":"3"
                                        },{
                                            "$ref":"1"
                                        }],
                                    "val":4
                                }],
                            "val":3
                        }],
                    "val":2
                },{
                    "$ref":"4"
                }],
            "val":1
        }
        graph = self.builder.build(g)
        self.assertEqual(graph.label, 1)
        labels = [None]*5
        for n in graph.neighbors:  # graph.label = 1, labels covers 2, 4
            labels[n.label] = n
        for n in labels[2].neighbors: # label = 2, labels covers 1, 3
            labels[n.label] = n
        self.assertCountEqual([n.label for n in labels[1].neighbors], [2, 4])
        self.assertCountEqual([n.label for n in labels[2].neighbors], [1, 3])
        self.assertCountEqual([n.label for n in labels[3].neighbors], [2, 4])
        self.assertCountEqual([n.label for n in labels[4].neighbors], [1, 3])
        

if __name__ == '__main__':
    unittest.main()
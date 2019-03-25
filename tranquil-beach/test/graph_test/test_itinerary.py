import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.itinerary import Itinerary

class TestItinerary(unittest.TestCase):
    def setUp(self):
        self.func = Itinerary()

    def test_1(self):
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        expected = ["JFK", "MUC", "LHR", "SFO", "SJC"]
        self.assertEqual(self.func.findItinerary(tickets), expected)

    def test_2(self):
        tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        expected = ["JFK","ATL","JFK","SFO","ATL","SFO"]
        self.assertEqual(self.func.findItinerary(tickets), expected)

    def test_3(self):
        tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
        expected = ["JFK","NRT","JFK","KUL"]
        self.assertEqual(self.func.findItinerary(tickets), expected)

if __name__ == '__main__':
    unittest.main()
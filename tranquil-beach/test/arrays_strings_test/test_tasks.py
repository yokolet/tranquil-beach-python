import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.tasks import Tasks

class TestTasks(unittest.TestCase):
    def setUp(self):
        self.func = Tasks()

    def test_1(self):
        tasks, n = ["A","A","A","B","B","B"], 2
        expected = 8
        self.assertEqual(self.func.leastInterval(tasks, n), expected)

if __name__ == '__main__':
    unittest.main()
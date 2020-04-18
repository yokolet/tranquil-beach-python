import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.my_calendar import MyCalendar

class TestMyCalendar(unittest.TestCase):
    def test_1(self):
        ops = ["MyCalendar","book","book","book"]
        params = [[],[10,20],[15,25],[20,30]]
        expected = [None, True, False, True]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

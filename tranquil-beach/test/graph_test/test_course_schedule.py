import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.course_schedule import CourseSchedule

class TestCourseSchedule(unittest.TestCase):
    def setUp(self):
        self.func = CourseSchedule().canFinish

    def test_1(self):
        num, courses = 2, [[1, 0]]
        expected = True
        self.assertTrue(self.func(num, courses))
    
    def test_2(self):
        num, courses = 2, [[1, 0], [0, 1]]
        expected = False
        self.assertFalse(self.func(num, courses))

if __name__ == '__main__':
    unittest.main()
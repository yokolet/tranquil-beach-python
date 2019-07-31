import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.course_schedule_path import CourseSchedulePath

class TestCourseSchedulePath(unittest.TestCase):
    def setUp(self):
        self.func = CourseSchedulePath().findOrder

    def test_1(self):
        num, courses = 2, [[1, 0]]
        expected = [0, 1]
        self.assertEquals(expected, self.func(num, courses))

    def test_2(self):
        num, courses = 4, [[1,0],[2,0],[3,1],[3,2]]
        expected = [[0,1,2,3], [0,2,1,3]]
        self.assertTrue(self.func(num, courses) in expected)

    def test_3(self):
        num, courses = 2, [[0,1],[1,0]]
        expected = []
        self.assertEquals(expected, self.func(num, courses))

    def test_4(self):
        num, courses = 2, []
        expected = [[1, 0], [0, 1]]
        self.assertTrue(self.func(num, courses) in expected)

if __name__ == '__main__':
    unittest.main()
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.sentence import Sentence

class TestSentence(unittest.TestCase):
    def setUp(self):
        self.func = Sentence().wordsTyping

    def test_1(self):
        sentence, rows, cols = ["hello", "world"], 2, 8
        expected = 1
        self.assertEqual(expected, self.func(sentence, rows, cols))

    def test_2(self):
        sentence, rows, cols = ["a", "bcd", "e"], 3, 6
        expected = 2
        self.assertEqual(expected, self.func(sentence, rows, cols))

    def test_3(self):
        sentence, rows, cols = ["I", "had", "apple", "pie"], 4, 5
        expected = 1
        self.assertEqual(expected, self.func(sentence, rows, cols))

if __name__ == '__main__':
    unittest.main()
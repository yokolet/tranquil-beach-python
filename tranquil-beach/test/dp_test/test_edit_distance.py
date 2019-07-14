import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.edit_distance import EditDistance

class TestEditDistance(unittest.TestCase):
  def setUp(self):
    self.func = EditDistance().minDistance
  
  def test_1(self):
    word1, word2 = "horse", "ros"
    expected = 3
    self.assertEqual(self.func(word1, word2), expected)

  def test_2(self):
    word1, word2 = "intention", "execution"
    expected = 5
    self.assertEqual(self.func(word1, word2), expected)

if __name__ == '__main__':
    unittest.main()

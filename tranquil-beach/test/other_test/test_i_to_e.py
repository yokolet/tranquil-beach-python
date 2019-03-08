import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.i_to_e import IntegerToEnglish

class TestIntegerToEnglish(unittest.TestCase):
    def setUp(self):
        self.func = IntegerToEnglish()

    def test_1(self):
        num = 123
        expected = "One Hundred Twenty Three"
        self.assertEqual(self.func.numberToWords(num), expected)

    def test_2(self):
        num = 12345
        expected = "Twelve Thousand Three Hundred Forty Five"
        self.assertEqual(self.func.numberToWords(num), expected)

    def test_3(self):
        num = 1234567
        expected = "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
        self.assertEqual(self.func.numberToWords(num), expected)

    def test_4(self):
        num = 1234567891
        expected = "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
        self.assertEqual(self.func.numberToWords(num), expected)

    def test_5(self):
        num = 20
        expected = "Twenty"
        self.assertEqual(self.func.numberToWords(num), expected)

    def test_6(self):
        num = 0
        expected = "Zero"
        self.assertEqual(self.func.numberToWords(num), expected)

    def test_7(self):
        num = 50868
        expected = "Fifty Thousand Eight Hundred Sixty Eight"
        self.assertEqual(self.func.numberToWords(num), expected)



if __name__ == '__main__':
    unittest.main()
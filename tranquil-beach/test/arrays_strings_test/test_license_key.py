import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.license_key import LicenseKey

class TestLicenseKey(unittest.TestCase):
    def setUp(self):
        self.func = LicenseKey().licenseKeyFormatting

    def test_1(self):
        s, k = '5F3Z-2e-9-w', 4
        expected = '5F3Z-2E9W'
        self.assertEqual(expected, self.func(s, k))

    def test_2(self):
        s, k = '2-5g-3-J', 2
        expected = '2-5G-3J'
        self.assertEqual(expected, self.func(s, k))

    def test_3(self):
        s, k = '--a-a-a-a--', 2
        expected = 'AA-AA'
        self.assertEqual(expected, self.func(s, k))

    def test_4(self):
        s, k = '---', 3
        expected = ''
        self.assertEqual(expected, self.func(s, k))

if __name__ == '__main__':
    unittest.main()
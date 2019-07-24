import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.group_anagrams import GroupAnagrams

class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.func = GroupAnagrams().groupAnagrams

    def test_1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = {
            'aet': ["ate","eat","tea"],
            'ant': ["nat","tan"],
            'abt': ["bat"]
        }
        result = self.func(strs)
        for a in result:
            e = expected[''.join(sorted(a[0]))]
            self.assertCountEqual(e, a)

if __name__ == '__main__':
    unittest.main()
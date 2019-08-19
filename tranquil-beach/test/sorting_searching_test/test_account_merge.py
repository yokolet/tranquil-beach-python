import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.account_merge import AccountMerge

class TestAccountMerge(unittest.TestCase):
    def setUp(self):
        self.func = AccountMerge().accountsMerge

    def test_1(self):
        accounts = [
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["Mary", "mary@mail.com"]
        ]
        expected = [
            ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
            ["John", "johnnybravo@mail.com"],
            ["Mary", "mary@mail.com"]
        ]
        self.assertCountEqual(expected, self.func(accounts))

    def test_2(self):
        accounts = [
            ["David","David0@m.co","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co","David6@m.co","David7@m.co"],
            ["David","David0@m.co","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co","David6@m.co","David7@m.co"],
            ["David","David2@m.co","David18@m.co","David19@m.co","David20@m.co","David21@m.co","David22@m.co","David23@m.co","David24@m.co","David25@m.co"],
            ["David","David3@m.co","David27@m.co","David28@m.co","David29@m.co","David30@m.co","David31@m.co","David32@m.co","David33@m.co","David34@m.co"],
            ["David","David1@m.co","David9@m.co","David10@m.co","David11@m.co","David12@m.co","David13@m.co","David14@m.co","David15@m.co","David16@m.co"]
        ]
        expected = [
            ['David',
            'David0@m.co', 'David10@m.co', 'David11@m.co', 'David12@m.co', 'David13@m.co', 'David14@m.co', 'David15@m.co',
            'David16@m.co', 'David18@m.co', 'David19@m.co', 'David1@m.co', 'David20@m.co', 'David21@m.co', 'David22@m.co',
            'David23@m.co', 'David24@m.co', 'David25@m.co', 'David27@m.co', 'David28@m.co', 'David29@m.co', 'David2@m.co',
            'David30@m.co', 'David31@m.co', 'David32@m.co', 'David33@m.co', 'David34@m.co', 'David3@m.co', 'David4@m.co',
            'David5@m.co', 'David6@m.co', 'David7@m.co', 'David9@m.co']
        ]
        self.assertCountEqual(expected, self.func(accounts))

    def test_3(self):
        accounts = [
            ["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],
            ["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],
            ["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],
            ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],
            ["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]
        ]
        expected = [
            ["Alex","Alex0@m.co","Alex4@m.co","Alex5@m.co"],
            ["Ethan","Ethan0@m.co","Ethan3@m.co"],
            ["Gabe","Gabe0@m.co","Gabe2@m.co","Gabe3@m.co","Gabe4@m.co"],
            ["Kevin","Kevin2@m.co","Kevin4@m.co"]
        ]
        self.assertCountEqual(expected, self.func(accounts))

    def test_4(self):
        accounts = [
            ["David","David0@m.co","David1@m.co"],
            ["David","David3@m.co","David4@m.co"],
            ["David","David4@m.co","David5@m.co"],
            ["David","David2@m.co","David3@m.co"],
            ["David","David1@m.co","David2@m.co"]
        ]
        expected = [
            ["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]
        ]
        self.assertCountEqual(expected, self.func(accounts))

if __name__ == '__main__':
    unittest.main()
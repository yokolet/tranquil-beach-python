import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.twitter import Twitter

class TestTwitter(unittest.TestCase):
    def test_1(self):
        ops = ["Twitter","postTweet","getNewsFeed","follow","postTweet",
                "getNewsFeed","unfollow", "getNewsFeed"]
        params = [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
        null = None
        expected = [null,null,[5],null,null,[6,5],null,[5]]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(result, expected)

    def test_2(self):
        ops = ["Twitter","postTweet","follow","getNewsFeed"]
        params = [[],[1,5],[1,1],[1]]
        null = None
        expected = [null,null,null,[5]]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(result, expected)

    def test_3(self):
        ops = ["Twitter","postTweet","postTweet","postTweet","postTweet",
                "postTweet","postTweet","postTweet","postTweet","postTweet",
                "postTweet","postTweet","getNewsFeed"]
        params = [[],[1,5],[1,3],[1,101],[1,13],
                    [1,10],[1,2],[1,94],[1,505],[1,333],
                    [1,22],[1,11],[1]]
        null = None
        expected = [null,null,null,null,null,null,null,null,null,null,
                    null,null,[11,22,333,505,94,2,10,13,101,3]]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
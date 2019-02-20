class LetterCombinations:
     def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []   
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        n = len(digits)
        result = list(letters[digits[0]])
        if n == 1:
            return result
        idx = 1
        while idx < n:
            result = [x + y for x in result for y in letters[digits[idx]]]
            idx += 1
        return result

"""
from collections import deque

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        q = deque(mapping[digits[0]])
        index = 1
        results = []
        while index < len(digits):
            letters = mapping[digits[index]]
            length = len(q)
            while length > 0:
                prev = q.popleft()
                length -= 1
                for l in letters:
                    q.append(prev + l)
            index += 1
        return list(q)
"""
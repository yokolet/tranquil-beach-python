class LetterPermutation:
    def letterCasePermutation(self, S: str) -> 'List[str]':
        s = [[c.lower(), c.upper()] if c.isalpha() else c for c in S]
        result = ['']
        for i in range(len(S)):
            result = [x + y for x in result for y in s[i]]
        return result
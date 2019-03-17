class RomanToInteger:
    def romanToInt(self, s: str) -> int:
        if not s: return 0
        table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result, prev = table[s[0]], table[s[0]]
        for c in s[1:]:
            cur = table[c]
            result += cur
            if cur > prev:
                result -= 2*prev
            prev = cur
        return result

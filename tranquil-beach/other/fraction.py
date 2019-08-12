class Fraction:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return '0'
        result = ''
        if numerator * denominator < 0: result += '-'
        n, d = abs(numerator), abs(denominator)
        result += str(n // d)

        r = n % d
        if r == 0: return result

        result += '.'
        memo = {}
        while r not in memo:
            memo[r] = len(result)
            result += str(r * 10 // d)
            r =  r * 10 % d
        result = result[:memo[r]] + '(' + result[memo[r]:] + ')'
        return result.replace('(0)', '')

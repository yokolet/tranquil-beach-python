class Division:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1 if dividend * divisor > 0 else -1
        n, d = abs(dividend), abs(divisor)
        result = 0
        while d <= n:
            tmp, count = d, 1
            while tmp <= n:
                n -= tmp
                result += count
                count <<= 1
                tmp <<= 1
        result *= sign
        return min(max(-2**31, result), 2**31 - 1)
    
    def divide2(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend > 0 and divisor > 0) or\
            (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
        n, d = abs(dividend), abs(divisor)
        count = 1
        while d <= n:
            d <<= 1
            count <<= 1
        d >>= 1
        count >>=1
        result = 0
        while count != 0:
            if n >= d:
                n -= d
                result |= count
            count >>= 1
            d >>= 1
        result *= sign
        return min(max(-2147483648, result), 2147483647)

    def divide1(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

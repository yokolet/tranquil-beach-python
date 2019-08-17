class Multiply:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        m, n = len(num1), len(num2)
        order1, memo = 1, []

        for i in range(m-1, -1, -1):
            carry, sub, order2 = 0, 0, 1
            d1 = ord(num1[i]) - ord('0')
            for j in range(n-1, -1, -1):
                d2 = ord(num2[j]) - ord('0')
                carry, rem = divmod(carry + d1 * d2, 10)
                sub += order2 * rem
                order2 *= 10
            sub += order2 * carry
            memo.append(sub)

        prev, d = divmod(memo[0], 10)
        result = str(d)
        for cur in memo[1:]:
            prev, d = divmod(prev + cur, 10)
            result = str(d) + result
        if prev > 0:
            result = str(prev) + result
        return result
            


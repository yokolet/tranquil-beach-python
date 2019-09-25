class HappyNumber:
    def isHappy(self, n: int) -> bool:
        if not n: return False

        def squareSum(v):
            sum, carry = 0, v
            while carry:
                carry, rem = divmod(carry, 10)
                sum += rem*rem
            return sum

        sum = squareSum(n)
        seen = {n}
        while sum != 1:
            sum = squareSum(sum)
            if sum in seen: return False
            seen.add(sum)
        return True

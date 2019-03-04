class AdditionByString:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry, result = len(num1) - 1, len(num2) - 1, 0, ""
        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                carry += int(num1[i])
            if j >= 0:
                carry += int(num2[j])
            carry, v = divmod(carry, 10)
            result = str(v) + result
            i -= 1
            j -= 1
        return result

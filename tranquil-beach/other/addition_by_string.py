class AdditionByString:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry, result = len(num1) - 1, len(num2) - 1, 0, ""
        while i >= 0 or j >= 0 or carry > 0:
            v_1 = int(num1[i]) if i >= 0 else 0
            v_2 = int(num2[j]) if j >= 0 else 0
            carry, v = divmod(carry + v_1 + v_2, 10)
            result = str(v) + result
            i -= 1
            j -= 1
        return result

class ColumnTitle:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while n:
            n -= 1
            result = chr((n % 26) + ord('A')) + result
            n //= 26
        return result

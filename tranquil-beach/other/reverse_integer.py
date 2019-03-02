class ReverseInteger:
    def reverse2(self, x: int) -> int:
        result = 0
        sign = -1 if x < 0 else 1
        v = abs(x)
        while v > 0:
            v, rem = divmod(v, 10)
            result = result * 10 + rem
        result *= sign
        return result if result in range(-2**31, 2**31-1) else 0

    def reverse(self, x: 'int') -> 'int':
        x = str(x)
        
        prefix = '-' if x[0] == '-' else ''
        
        x = x.strip('-')[::-1]
        retint = int(prefix+x)
        return retint if retint in range(-2**31, 2**31-1) else 0
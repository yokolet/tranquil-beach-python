class StrobogrammaticLenN:
    def findStrobogrammatic(self, n: int) -> 'List[str]':
        def walk(l, left, right):
            if l == 0:
                result.append(left+right)
                return
            if l == 1:
                for d in '018':
                    result.append(left+d+right)
                return
            if l == n:
                for d in '1689':
                    walk(l-2, left+d, mapping[d]+right)
            else:
                for d in '01689':
                    walk(l-2, left+d, mapping[d]+right)

        mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        result = []
        walk(n, '', '')
        return result

    def findStrobogrammatic2(self, n: int) -> 'List[str]':
        def walk(low, high, left, right):
            if low == high:
                for d in '018':
                    result.append(left+d+right)
                return
            if low > high:
                result.append(left+right)
                return
            if low == 0:
                for d in '1689':
                    walk(low+1, high-1, left+d, mapping[d]+right)
            else:
                for d in '01689':
                    walk(low+1, high-1, left+d, mapping[d]+right)

        if n == 0: return ['']
        mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        result = []
        walk(0, n-1, '', '')
        return result
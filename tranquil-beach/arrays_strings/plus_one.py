class PlusOne:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

    def plusOne2(self, digits: 'List[int]') -> 'List[int]':
        digits[-1] += 1
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            carry, rem = divmod(digits[i] + carry, 10)
            digits[i] = rem
            if carry == 0: return digits
        if carry == 1:
            return [1] + [0] * len(digits)

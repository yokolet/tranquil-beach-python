class AddBinary:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary2(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ''
        idx_a, idx_b = len(a) - 1, len(b) - 1
        carry = 0
        while idx_a >= 0 or idx_b >= 0:
            d_a = 1 if idx_a >= 0 and a[idx_a] == '1' else 0
            d_b = 1 if idx_b >= 0 and b[idx_b] == '1' else 0
            tmp = carry + d_a + d_b
            carry, rem = tmp // 2, tmp % 2
            result = str(rem) + result
            idx_a -= 1
            idx_b -= 1
        if carry == 1:
            result = '1' + result
        return result

    def addBinary3(self, a: 'str', b: 'str') -> 'str':
        Len=max(len(a),len(b))
        a=a.zfill(Len)
        b=b.zfill(Len)
        add=0
        s=""
        for i in range(Len-1, -1, -1):
            temp=int(a[i])+int(b[i])+add
            if temp>=2:
                s=str(temp-2)+s
                add=1
            else:
                s=str(temp)+s
                add=0
        if add==1:
            return "1"+s
        return s
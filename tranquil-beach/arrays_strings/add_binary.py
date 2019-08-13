class AddBinary:
    def addBinary4(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary(self, a: str, b: str) -> str:
        result = ''
        idx_a, idx_b = len(a) - 1, len(b) - 1
        carry = 0
        while idx_a >= 0 or idx_b >= 0:
            v_a = 1 if idx_a >= 0 and a[idx_a] == '1' else 0
            v_b = 1 if idx_b >= 0 and b[idx_b] == '1' else 0
            carry, rem = divmod(carry + v_a + v_b, 2)
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

    def addBinary2(self, a: 'str', b: 'str') -> 'str':
        table = {
            (False, False, False): (False, '0'), # carry and value
            (False, False, True): (False, '1'),
            (False, True, False): (False, '1'),
            (False, True, True): (True, '0'),
            (True, False, False): (False, '1'),
            (True, False, True): (True, '0'),
            (True, True, False): (True, '0'),
            (True, True, True): (True, '1'),
            (False, False): (False, '0'),
            (False, True): (False, '1'),
            (True, False): (False, '1'),
            (True, True): (True, '0')
        }
        idx_a, idx_b = len(a)-1, len(b)-1
        carry, result = False, ''
        while idx_a >= 0 and idx_b >= 0:
            carry, c = table[(carry, a[idx_a]=='1', b[idx_b]=='1')]
            result = c + result
            idx_a -= 1
            idx_b -= 1
        (idx, s) = (idx_a, a) if idx_a >= 0 else (idx_b, b)
        while carry and idx >=0:
            carry, c = table[(carry, s[idx]=='1')]
            result = result + c
            idx -= 1
        if carry: result = '1' + result
        return result

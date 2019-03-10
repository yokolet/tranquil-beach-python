class Operators:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num: return []

        def dfs(i, expr, acc, last, cur):
            if i == n-1:
                if acc + last + values[i] == target:
                    result.append(expr + '+' + num[i])
                if acc + last - values[i] == target:
                    result.append(expr + '-' + num[i])
                if acc + last * values[i] == target:
                    result.append(expr + '*' + num[i])
                if cur and acc + last // cur * (10 * cur + values[i]) == target:
                    result.append(expr + num[i])
            else:
                dfs(i + 1, expr + '+' + num[i], acc + last, values[i], values[i])
                dfs(i + 1, expr + '-' + num[i], acc + last, -values[i], values[i])
                dfs(i + 1, expr + '*' + num[i], acc, last * values[i], values[i])
                if cur:
                    dfs(i + 1, expr + num[i], acc, last // cur * (10 * cur + values[i]), 10 * cur + values[i])

        values = [int(x) for x in num]
        n = len(values)
        if n ==1 :
            if values[0] == target:
                return [num]
            return []
        result = []
        dfs(1, num[0], 0, values[0], values[0])
        return result

    def addOperators3(self, num, target):
        def dfs(num, temp, cur, last):
            if not num:
                if cur == target:
                    res.append(temp)
                return
            for i in range(1, len(num)+1):
                val = num[:i]
                if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                    dfs(num[i:], temp + "+" + val, cur+int(val), int(val))
                    dfs(num[i:], temp + "-" + val, cur-int(val), -int(val))
                    dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val))

        res = []
        for i in range(1,len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                dfs(num[i:], num[:i], int(num[:i]), int(num[:i])) # this step put first number in the string
        return res


    def addOperators5(self, num: str, target: int) -> 'List[str]':
        if not num: return []

        def dfs(num, expr, acc, last):
            if not num:
                if acc == target:
                    result.append(expr)
                return
            for i in range(1, len(num)+1):
                n = num[:i]
                if i == 1 or (i > 1 and num[0] != "0"):
                    exprs = [expr + op + n for op in ops]
                    accs = [acc + int(n), acc - int(n), acc - last + last * int(n)]
                    lasts = [int(n), -int(n), last * int(n)]
                    for j in range(3):
                        if exprs[j] not in visited:
                            visited.add(exprs[j])
                            dfs(num[i:], exprs[j], accs[j], lasts[j])

        result = []
        ops = ["+", "-", "*"]
        visited = set(num[0])
        for i in range(1, len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"):
                dfs(num[i:], num[:i], int(num[:i]), int(num[:i]))
        return result

    def addOperators4(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        nums = [int(x) for x in num]
        n = len(nums)
        if n==1:
            if nums[0]==target:
                return [num]
            return []
        res = []
        # prod is the number before
        # presum is sum before the number before
        # i is current location
        # expr is current string
        # cur is int (current char)
        def dfs(i, expr, preSum, prod, cur):
            '''
            i: int
            expr: str
            preSum: int
            prod:int
            cur: int
            '''
            # base case: position reach end of num
            if i==n-1:
                if preSum+prod+nums[i]==target:
                    res.append(expr+'+'+num[i])
                if preSum+prod-nums[i]==target:
                    res.append(expr+'-'+num[i])
                if preSum+prod*nums[i]==target:
                    res.append(expr+'*'+num[i])
                # cur at end is int(the one before last)
                # if cur avoid 01
                if cur and preSum+prod//cur*(10*cur+nums[i])==target:
                    res.append(expr+num[i])
            else:
                dfs(i+1,expr+'+'+num[i],preSum+prod,nums[i],nums[i])  #the area of concern always includes a operator and part of 
                dfs(i+1,expr+'-'+num[i],preSum+prod,-nums[i],nums[i]) #the next operand
                dfs(i+1,expr+'*'+num[i],preSum,prod*nums[i],nums[i])
                if cur:
                    dfs(i+1,expr+num[i],preSum,prod//cur*(10*cur+nums[i]),10*cur+nums[i])
        dfs(1,num[0],0,nums[0],nums[0])
        return res
    

    
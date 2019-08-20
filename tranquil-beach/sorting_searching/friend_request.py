class FriendRequest:
    def numFriendRequests(self, ages: 'List[int]') -> int:
        memo = [0 for _ in range(121)] # 1 <= ages[i] <= 120
        for a in ages:
            memo[a] += 1
        result = 0
        for i in range(15, 121):          # age of A
            if memo[i] == 0: continue
            for j in range(i//2+8, i+1):  # age of B
                if i == j:                # subtract a request to self
                    result += memo[i] * (memo[j] - 1)
                else:
                    result += memo[i] * memo[j]
        return result

    def numFriendRequests2(self, ages: 'List[int]') -> int:
        n = len(ages)
        if n < 2: return 0
        memo = [0 for _ in range(121)]
        for a in ages:
            memo[a] += 1
        result = 0
        for i in range(15, 121):
            if memo[i] > 0:
                yougest = i//2+7 + 1
                result += memo[i] * (sum(memo[yougest:i + 1]) - 1)
        return result
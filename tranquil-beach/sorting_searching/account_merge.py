class AccountMerge:
    def accountsMerge(self, accounts: 'List[List[str]]') -> 'List[List[str]]':
        n = len(accounts)
        memo = {}
        group = [i for i in range(n)]

        def find(p):
            while p != group[p]:
                p = group[p]
            return p

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                min_p, max_p = min(x, y), max(x, y)
                group[max_p] = min_p

        for i in range(n):
            for e in accounts[i][1:]:
                if e in memo:
                    union(i, memo[e])
                else:
                    memo[e] = i

        for i in range(n):
            if i != group[i]:
                p = find(group[i])
                for e in accounts[i][1:]:
                    accounts[p].append(e)
                accounts[i] = None

        return [[a[0]]+sorted(set(a[1:])) for a in accounts if a]

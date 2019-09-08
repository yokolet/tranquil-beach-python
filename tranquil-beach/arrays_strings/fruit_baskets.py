class FruitBaskets:
    def totalFruit(self, tree: 'List[int]') -> int:
        left, max_len, memo = 0, 0, {}
        for i in range(len(tree)):
            memo[tree[i]] = i
            if len(memo) > 2:
                left = min(memo.values())
                del memo[tree[left]]
                left += 1
            max_len = max(max_len, i-left+1)
        return max_len
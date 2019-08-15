class Strobogrammatic:
    def isStrobogrammatic(self, num: str) -> bool:
        memo = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in memo and num[right] not in memo: return False
            if memo[num[left]] != num[right]: return False
            left += 1
            right -= 1
        return True

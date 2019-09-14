class ClosestPalindrome:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        closests = set()
        closests.add(pow(10, length) + 1) # if 99, 101 may be the closest
        closests.add(pow(10, length - 1) - 1) # if 100, 99 may be the closest
        prefix = int(n[:((length + 1) // 2)]) # right should be a mirror of left
        for i in [-1, 0, 1]:
            left = str(prefix + i)
            if length % 2 == 0:
                closests.add(int(left + left[::-1]))
            else:
                closests.add(int(left + left[:-1][::-1]))
        num, min_diff = int(n), float('inf')
        if num in closests: closests.remove(num)
        for v in closests:
            diff = abs(v - num)
            if diff < min_diff:
                min_diff = diff
                result = v
            elif diff == min_diff:
                result = min(result, v)
        return str(result)

# if length 1, subtract 1
# all 9s: 99 -> 101, 999 -> 1001  
# n is a palindrome: change middle, down or up (if middle is 0)
# other: change right half by a mirror of left half
class BadVersion(object):
    def __init__(self, func):
        self.func = func

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        isBadVersion = self.func

        if n == 1 and isBadVersion(n): return n
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            result = isBadVersion(mid)
            if result:
                if not isBadVersion(mid - 1):
                    return mid
                high = mid - 1
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                low = mid + 1
        return mid
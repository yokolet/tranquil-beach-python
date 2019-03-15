class OnceByRead4:
    def __init__(self, func):
        self.func = func
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        read4 = self.func

        start, end, tmp = 0, 0, [''] * 4
        q, m = divmod(n, 4)
        for _ in range(q):
            count = read4(tmp)
            end += count
            buf[start:end] = tmp[:count]
            start = end
        if m > 0:
            count = read4(tmp)
            count = min(count, m)
            end += count
            buf[start:end] = tmp[:count]
        return end

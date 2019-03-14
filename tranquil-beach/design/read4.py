class Read4:
    def __init__(self, func):
        self.queue = []
        self.func = func

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        read4 = self.func

        if n == 0: return 0
        while len(self.queue) < n:
            tmp = [''] * 4
            count = read4(tmp)
            self.queue += tmp[:count]
            if count < 4:
                break
        length = min(n, len(self.queue))
        buf[:length] = self.queue[:length]
        del self.queue[:length]
        return length
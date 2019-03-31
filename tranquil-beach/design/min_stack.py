class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.mins) == 0 or self.mins[-1] >= x:
            self.mins.append(x)

    def pop(self):
        """
        :rtype: void
        """
        tmp = self.stack.pop()
        if self.mins[-1] == tmp:
            self.mins.pop()
        return tmp

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]
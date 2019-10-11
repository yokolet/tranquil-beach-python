class Vector2D:
    def __init__(self, v: 'List[List[int]]'):
        self.values = [j for i in v for j in i][::-1]

    def next(self) -> int:
        return self.values.pop()

    def hasNext(self) -> bool:
        return len(self.values) > 0


    def __init__2(self, v: 'List[List[int]]'):
        self.v = v
        self.i = 0
        self.j = 0

    def next2(self) -> int:
        if not self.hasNext(): return None
        value = self.v[self.i][self.j]
        self.j += 1
        return value

    def hasNext3(self) -> bool:
        if self.i < len(self.v):
            if self.j < len(self.v[self.i]):
                return True
            else:
                self.i += 1
                self.j = 0
                return self.hasNext()
        else:
            return False

    def hasNext2(self) -> bool:
        while self.i < len(self.v):
            if self.j < len(self.v[self.i]):
                return True
            self.i += 1
            self.j = 0
        return False

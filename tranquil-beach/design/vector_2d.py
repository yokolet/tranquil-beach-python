class Vector2D:
    def __init__(self, v: 'List[List[int]]'):
        self.values = [j for i in v for j in i][::-1]

    def next(self) -> int:
        return self.values.pop()

    def hasNext(self) -> bool:
        return len(self.values) > 0

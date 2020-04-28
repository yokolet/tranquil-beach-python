from collections import OrderedDict

class FirstUnique:
    def __init__(self, nums: 'List[int]'):
        self.n_dict = OrderedDict()
        self.seen = set()
        for v in nums:
            self.seen.add(v)
            self.n_dict[v] = self.n_dict.get(v, 0) + 1
        for k in list(self.n_dict.keys()):
            if self.n_dict[k] > 1:
                self.n_dict.pop(k)

    def showFirstUnique(self) -> int:
        return next(iter(self.n_dict)) if self.n_dict else -1

    def add(self, value: int) -> None:
        if value not in self.seen:
            self.seen.add(value)
            self.n_dict[value] = 1
        elif value in self.n_dict:
            self.n_dict.pop(value)

class SnapshotArray:
    def __init__(self, length: int):
        self.length = length
        self.values = {}
        self.snapshot = []

    def set(self, index: int, val: int) -> None:
        self.values[index] = val

    def snap(self) -> int:
        s = {}
        for k, v in self.values.items():
            s[k]=v
        self.snapshot.append(s)
        return len(self.snapshot) - 1

    def get(self, index: int, snap_id: int) -> int:
        s = self.snapshot[snap_id]
        if index in s:
            return s[index]
        else:
            return 0

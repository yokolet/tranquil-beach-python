from collections import defaultdict

class TimeMap:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = defaultdict(list)
        self.values = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times: return ''
        ts = self.times[key]
        if not ts or timestamp < ts[0]: return ''
        low, high = 0, len(ts)-1
        while low <= high:
            mid = (low + high) // 2
            if ts[mid] == timestamp:
                low = high = mid
            if ts[mid] <= timestamp:
                low = mid + 1
            else:
                high = mid - 1
        return self.values[key][high]
class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamps = [] # queue

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.timestamps.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.timestamps and self.timestamps[0] <= timestamp - 300:
            self.timestamps.pop(0)
        return len(self.timestamps)

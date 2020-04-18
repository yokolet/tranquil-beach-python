import bisect

class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect_left(self.calendar, (start, end))
        canBook = True
        canBook &= idx == 0 or start >= self.calendar[idx-1][1]
        canBook &= idx == len(self.calendar) or end <= self.calendar[idx][0]
        if canBook:
            self.calendar = self.calendar[:idx] + [(start, end)] + self.calendar[idx:]
            return True
        else:
            return False

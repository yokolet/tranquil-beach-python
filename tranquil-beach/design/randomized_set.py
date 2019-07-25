import random

class RandomizedSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals, self.valToIdx = [], {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.valToIdx:
            return False
        else:
            self.vals.append(val)
            self.valToIdx[val] = len(self.vals) - 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.valToIdx:
            return False
        else:
            idx, lastVal = self.valToIdx[val], self.vals.pop()
            del self.valToIdx[val]
            if val == lastVal: return True
            self.vals[idx] = lastVal
            self.valToIdx[lastVal] = idx
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.vals)
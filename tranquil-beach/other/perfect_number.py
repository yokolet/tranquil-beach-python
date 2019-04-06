from math import ceil, sqrt

class PerfectNumber:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1: return False
        sum = 1
        for i in range(2, ceil(sqrt(num))):
            if num % i == 0:
                sum += i
                sum += num // i
        return sum == num

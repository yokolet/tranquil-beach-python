from collections import defaultdict

class CountElements:
    def countElements(self, arr: 'List[int]') -> int:
        num_dict = defaultdict(int)
        for i in range(len(arr)):
            num_dict[arr[i]] += 1
        count = 0
        for k in num_dict.keys():
            if k+1 in num_dict:
                count += num_dict[k]
        return count
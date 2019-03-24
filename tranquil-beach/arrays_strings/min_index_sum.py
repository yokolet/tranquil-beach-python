class MinIndexSum:
    def findRestaurant(self, list1: 'List[str]', list2: 'List[str]') -> 'List[str]':
        rank1 = {v: i for i, v in enumerate(list1)}
        common = []
        index_sum = float('inf')
        for i, v in enumerate(list2):
            if i > index_sum: break
            if v in rank1:
                cur = i + rank1[v]
                if index_sum == cur:
                    common.append(v)
                elif index_sum > cur:
                    index_sum = cur
                    common = [v]
        return common
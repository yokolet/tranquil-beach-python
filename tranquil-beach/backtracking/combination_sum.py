class CombinationSum:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(arr, target, index, path, result):
            if target == 0:
                result.append(path)
                return
            while index < len(arr) and arr[index] <= target:
                dfs(arr, target-arr[index], index, path+[arr[index]], result)
                index += 1
        result = []
        dfs(sorted(candidates), target, 0, [], result)
        return result
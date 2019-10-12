class CombinationSum:
    def combinationSum(self, candidates: 'List[int]', target: int) -> 'List[List[int]]':
        def dfs(arr, target, idx, path, result):
            if target == 0:
                result.append(path)
                return
            while idx < len(arr) and arr[idx] <= target:
                dfs(arr, target-arr[idx], idx, path+[arr[idx]], result)
                idx += 1
        result = []
        dfs(sorted(candidates), target, 0, [], result)
        return result
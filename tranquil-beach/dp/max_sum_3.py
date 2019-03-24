class MaxSum3:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        left, mid, right = 0, k, 2*k
        sum_l, sum_m, sum_r = sum(nums[left:left+k]), sum(nums[mid:mid+k]), sum(nums[right:right+k])
        max_l, max_m, max_r = sum_l, sum_l + sum_m, sum_l + sum_m + sum_r
        idx_l, idx_m, idx_r = left, [left, mid], [left, mid, right]
        while right < len(nums) - k:
            sum_l += (nums[left + k] - nums[left])
            sum_m += (nums[mid + k] - nums[mid])
            sum_r += (nums[right + k] - nums[right])
            if sum_l > max_l:
                max_l = sum_l
                idx_l = left + 1
            if max_l + sum_m > max_m:
                max_m = max_l + sum_m
                idx_m = [idx_l, mid + 1]
            if max_m + sum_r > max_r:
                max_r = max_m + sum_r
                idx_r = idx_m + [right + 1]
            left += 1
            mid += 1
            right += 1
        return idx_r

    def maxSumOfThreeSubarrays2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        # creates accumulation array, length n + 1
        acc = [0]
        for i in range(n):
            acc.append(acc[i] + nums[i])

        # left and right side of max sums
        total = acc[k] - acc[0]
        left, right = [0] * n, [0] * n
        for i in range(k, n-2*k+1):  # 2*k elements should be left
            if total < acc[i] - acc[i - k]:
                left[i] = i - k
                total = acc[i] - acc[i - k]
            else:
                left[i] = left[i - 1]
        total = acc[n] - acc[n - k]
        for i in range(n-k, 2*k-1, -1):
            if total <= acc[i + k] - acc[i]:
                right[i] = i
                total = acc[i + k] - acc[i]
            else:
                right[i] = right[i + 1]

        # find maximum combination starting from a middle
        maxSum = -1
        for i in range(k, n-2*k+1):
            l, r = left[i], right[i + k]
            total = (acc[i + k] - acc[i]) +\
                    (acc[l + k] - acc[l]) +\
                    (acc[r + k] - acc[r])
            if maxSum < total:
                maxSum = total
                result = (l, i, r)
        return result


    def maxSumOfThreeSubarrays3(self, nums: 'List[int]', k: int) -> 'List[int]':
        a, b, c = 0, k, 2 * k
        suma, sumb, sumc = sum(nums[a:a+k]), sum(nums[b:b+k]), sum(nums[c:c+k])
        best1, best2, best3 = suma, suma+sumb, suma+sumb+sumc 
        index1, index2, index3 = a, (a, b), (a, b, c)
        while c + k < len(nums):
            suma = suma + nums[a + k] - nums[a]
            sumb = sumb + nums[b + k] - nums[b]
            sumc = sumc + nums[c + k] - nums[c]
            if suma > best1:
                best1 = suma
                index1 = a + 1
            if best1 + sumb > best2:
                best2 = best1 + sumb
                index2 = (index1, b + 1)
            if best2 + sumc > best3:
                best3 = best2 + sumc
                index3 = (index2[0], index2[1], c + 1)
            a += 1
            b += 1
            c += 1
        return index3
        
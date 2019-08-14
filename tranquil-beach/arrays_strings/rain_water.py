class RainWater:
    def trap(self, height: 'List[int]') -> int:
        if not height or len(height) < 3: return 0
        left, right, total = 0, len(height) - 1, 0
        left_max, right_max = height[left], height[right]
        while left < right:
            if left_max <= right_max:
                total += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                total += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return total

    def trap1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, min_height, total = 0, len(height) - 1, 0, 0
        while left < right:
            while left < right and height[left] <= min_height:
                total += min_height - height[left]
                left += 1
            while left < right and height[right] <= min_height:
                total += min_height - height[right]
                right -= 1
            min_height = min(height[left], height[right])
        return total

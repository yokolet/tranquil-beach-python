class ContainerWater:
    def maxArea(self, height: 'List[int]') -> int:
        left, right, max_water = 0, len(height) - 1, 0
        while left < right:
            min_height = min(height[left], height[right])
            max_water = max(max_water, min_height*(right - left))
            if  height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water

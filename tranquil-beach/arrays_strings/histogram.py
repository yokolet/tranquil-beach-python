class Histogram:
    def largestRectangleArea(self, heights: 'List[int]') -> int:
        if not heights: return 0
        max_area, stack, n = 0, [], len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if len(stack) == 0 else i - stack[-1] - 1
                max_area = max(max_area, w * h)
            stack.append(i)
        while stack:
            h = heights[stack.pop()]
            w = n if len(stack) == 0 else n - stack[-1] - 1
            max_area = max(max_area, w * h)
        return max_area

    def largestRectangleArea2(self, heights: 'List[int]') -> int:
        heights = [0] + heights + [0]
        stack = []
        res = 0
        for i, num in enumerate(heights):
            while stack and heights[stack[-1]] > num:
                    top = stack.pop()
                    res = max(res, (i - stack[-1] - 1) * heights[top])
            stack.append(i)
        return res
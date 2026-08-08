class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res, stack = 0, []
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                res = max(res, height * (i - idx))
                start = idx
            stack.append((start, h))
        while stack:
            i, h = stack.pop()
            res = max(res, h * (len(heights) - i))
        return res
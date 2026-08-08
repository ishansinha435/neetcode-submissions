class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res, stack = 0, []
        for i, h in enumerate(heights):
            index = i
            while stack and h < stack[-1][1]:
                old_i, old_h = stack.pop()
                res = max(res, old_h * (i - old_i))
                index = old_i
            stack.append((index, h))
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        return res
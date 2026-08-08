class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res, stack = 0, []
        for i, h in enumerate(heights):
            if not stack or h >= stack[-1][1]:
                stack.append((i, h))
            else:
                while stack and h < stack[-1][1]:
                    index, height = stack.pop()
                    res = max(res, height * (i - index))
                stack.append((index, h))
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        return res
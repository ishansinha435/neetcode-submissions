class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []
        for i, h in enumerate(heights):
            if not stack or h >= stack[-1][1]:
                stack.append((i, h))
            else:
                while stack and h < stack[-1][1]:
                    old_i, old_h = stack.pop()
                    area = max(area, old_h * (i - old_i))
                    new_i = old_i
                stack.append((old_i, h))
        for i, h in stack:
            area = max(area, h * (len(heights) - i))
        return area
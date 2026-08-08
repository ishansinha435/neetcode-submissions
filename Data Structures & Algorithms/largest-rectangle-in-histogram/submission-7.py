class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, area = [], 0
        for i, h in enumerate(heights):
            if not stack or h >= stack[-1][1]:
                stack.append((i, h))
            else:
                while stack and h < stack[-1][1]:
                    index, height = stack.pop()
                    area = max(area, height * (i - index))
                    old_i = index
                stack.append((old_i, h))
        for i, h in stack:
            area = max(area, h * (len(heights) - i))
        return area
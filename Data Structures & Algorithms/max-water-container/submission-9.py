class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area, l, r = 0, 0, len(heights) - 1
        max_l, max_r = heights[l], heights[r]
        while l < r:
            if max_l < max_r:
                area = max(area, max_l * (r - l))
                l += 1
                max_l = max(max_l, heights[l])
            else:
                area = max(area, max_r * (r - l))
                r -= 1
                max_r = max(max_r, heights[r])
        return area
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currmax, l, r = 0, 0, len(heights) - 1
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            currmax = max(currmax, area)
            if(heights[l] < heights[r]): l += 1
            else: r -= 1
        return currmax
        
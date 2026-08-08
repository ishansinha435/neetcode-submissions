class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(heights) - 1
        while l < r:
            curr = (r - l) * min(heights[l], heights[r])
            maxWater = max(maxWater, curr)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return maxWater

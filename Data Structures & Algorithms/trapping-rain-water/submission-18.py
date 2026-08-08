class Solution:
    def trap(self, height: List[int]) -> int:
        area, l, r = 0, 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                area += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                area += max_r - height[r]
        return area
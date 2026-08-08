class Solution:
    def trap(self, height: List[int]) -> int:
        area, lMax, rMax, maxi = 0, [0] * len(height), [0] * len(height), 0
        for i in range(1, len(height)):
            maxi = max(maxi, height[i-1])
            lMax[i] = maxi
        maxi = 0
        for i in range(len(height) - 2, -1, -1):
            maxi = max(maxi, height[i+1])
            rMax[i] = maxi
        for i in range(len(height)):
            toAdd = min(lMax[i], rMax[i]) - height[i]
            if toAdd > 0: area += toAdd
        return area
        
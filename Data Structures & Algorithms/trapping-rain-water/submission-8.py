class Solution:
    def trap(self, height: List[int]) -> int:
        area, l, r = 0, 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        while l < r:
            if lMax <= rMax:
                l += 1
                if lMax - height[l] > 0: area += lMax - height[l]
                lMax = max(lMax, height[l])
            else:
                r -= 1
                if rMax - height[r] > 0: area += rMax - height[r]
                rMax = max(rMax, height[r])
        return area   


        '''
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
        '''
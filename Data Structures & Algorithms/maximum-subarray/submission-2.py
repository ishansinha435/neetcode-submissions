class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, r = nums[0], 0
        curr_sum = 0
        while r < len(nums):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[r]
            res = max(res, curr_sum)
            r+= 1
        return res
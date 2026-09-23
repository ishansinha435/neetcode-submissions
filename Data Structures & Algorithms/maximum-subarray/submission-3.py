class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, r = nums[0], 0
        curr_sum = 0
        for r in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[r]
            res = max(res, curr_sum)
        return res
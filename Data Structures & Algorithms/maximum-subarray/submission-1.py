class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        curr_pre = 0
        for r, n in enumerate(nums):
            if curr_pre < 0:
                curr_pre = n
            else:
                curr_pre += n
            res = max(res, curr_pre)
        return res
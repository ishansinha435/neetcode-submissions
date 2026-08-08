class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prescript, postscript = 1, 1
        for i in range(len(nums)):
            res[i] *= prescript
            prescript *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postscript
            postscript *= nums[i]
        return res
        


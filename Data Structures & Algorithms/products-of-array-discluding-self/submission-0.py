class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        res[0] = 1
        postfix = 1
        for i in range(1,len(nums)):
            res[i] = res[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            postfix *= nums[i+1]
            res[i] *= postfix
        return res
        
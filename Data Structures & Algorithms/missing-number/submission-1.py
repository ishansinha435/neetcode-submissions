class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # return n * (n + 1) // 2 - sum(nums)

        res = 0
        for i, n in enumerate(nums):
            res = res ^ i ^ n
        return res ^ len(nums)

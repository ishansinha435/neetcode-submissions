class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # maxi, mini = 1, 1
        # res = nums[0]
        # for n in nums:
        #     temp = maxi * n
        #     maxi = max(n, maxi * n, mini * n)
        #     mini = min(n, mini * n, temp)
        #     res = max(res, maxi)
        # return res

        res = nums[0]
        prefix = suffix = 1

        for i, n in enumerate(nums):
            prefix = (prefix or 1) * n
            suffix = (suffix or 1) * nums[len(nums) - 1 - i]
            res = max(res, suffix, prefix)
        return res
            
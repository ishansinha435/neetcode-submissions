class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi, mini = 1, 1
        res = nums[0]
        for n in nums:
            temp = maxi * n
            maxi = max(n, maxi * n, mini * n)
            mini = min(n, mini * n, temp)
            res = max(res, maxi)
        return res
            
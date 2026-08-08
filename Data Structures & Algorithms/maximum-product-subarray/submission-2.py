class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi, mini = 1, 1
        res = nums[0]
        for n in nums:
            if n == 0:
                maxi = 1
                mini = 1
                res = max(res, 0)
                continue
            elif n > 0:
                maxi = max(n, maxi * n)
                mini = min(n, mini * n)
            else:
                temp = maxi
                maxi = max(n, mini * n)
                mini = min(n, temp * n)
            res = max(res, maxi)
        return res
            
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi, mini = 1, 1
        res = nums[0]
        for n in nums:
            if n > 0:
                maxi, mini = max(n, maxi * n), min(n, mini * n)
            elif n < 0:
                maxi, mini = max(n, mini * n), min(n, maxi * n)
            else:
                res = max(res, 0)
                maxi, mini = 1, 1
                continue
            res = max(res, maxi)
        return res

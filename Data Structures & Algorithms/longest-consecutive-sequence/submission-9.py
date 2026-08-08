class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, hset = 0, set(nums)
        for n in nums:
            if n - 1 not in hset:
                length = 1
                while n + length in hset:
                    length += 1
                res = max(res, length)
        return res

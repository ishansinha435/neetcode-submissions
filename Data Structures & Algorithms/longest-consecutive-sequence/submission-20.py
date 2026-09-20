class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, hset = 0, set(nums)
        for n in hset:
            if n - 1 not in hset:
                longest = 1
                while n + longest in hset:
                    longest += 1
                res = max(res, longest)
        return res
                
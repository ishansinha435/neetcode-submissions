class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset, res = set(nums), 0
        for n in nums:
            if n - 1 not in hset:
                length = 1
                while n + length in hset:
                    length += 1
                res = max(res, length)
        return res
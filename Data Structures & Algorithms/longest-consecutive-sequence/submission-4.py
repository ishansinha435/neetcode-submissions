class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        maxseq = 0
        for n in nums:
            if not n - 1 in hset:
                length = 1
                while n + length in hset:
                    length += 1
                maxseq = max(maxseq, length)
        return maxseq

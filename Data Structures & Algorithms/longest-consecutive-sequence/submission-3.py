class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        maxseq = 0
        for n in nums:
            if n - 1 not in hset:
                curr = n
                while curr + 1  in hset:
                    curr += 1
                maxseq = max(maxseq, curr + 1 - n)
        return maxseq

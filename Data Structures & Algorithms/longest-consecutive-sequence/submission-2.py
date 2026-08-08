class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in numSet:
                current = 1
                while n+1 in numSet:
                    current += 1
                    n += 1
                if current >= longest: 
                    longest = current
        return longest

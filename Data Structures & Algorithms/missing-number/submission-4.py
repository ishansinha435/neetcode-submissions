class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = len(nums)
        sumi = 0
        for i in range(len(nums)):
            total ^= i
            sumi ^= nums[i]
        return total ^ sumi
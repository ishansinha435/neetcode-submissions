class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            dp[i] += max((dp[j] for j in range(i + 1, len(nums)) if nums[i] < nums[j]), default=0)
        return max(dp)

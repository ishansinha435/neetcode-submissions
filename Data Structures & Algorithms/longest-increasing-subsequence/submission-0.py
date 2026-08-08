class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))
        for i in range(len(nums) - 1, -1, -1):
            length = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    length = max(length, 1 + dp[j])
            dp[i] = length
        return max(dp)
                
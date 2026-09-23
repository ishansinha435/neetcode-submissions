class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [False] * len(nums)
        
        def dfs(i):
            if i >= len(nums) or memo[i]:
                return
            memo[i] = True
            for j in range(1, nums[i] + 1):
                dfs(i + j)
        
        dfs(0)
        return memo[-1]
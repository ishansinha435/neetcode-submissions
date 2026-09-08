class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        
    def helper(self, nums: List[int]) -> int:
        one_behind, two_behind = 0, 0
        for n in nums:
            one_behind, two_behind = max(one_behind, two_behind + n), one_behind
        return one_behind
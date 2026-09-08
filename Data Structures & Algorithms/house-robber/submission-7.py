class Solution:
    def rob(self, nums: List[int]) -> int:
        one_behind, two_behind = 0, 0
        for i in range(len(nums)):
            one_behind, two_behind = max(one_behind, two_behind + nums[i]), one_behind
        return max(one_behind, two_behind)
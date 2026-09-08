class Solution:
    def rob(self, nums: List[int]) -> int:
        one_behind, two_behind = 0, 0
        for n in nums:
            one_behind, two_behind = max(one_behind, two_behind + n), one_behind
        return one_behind
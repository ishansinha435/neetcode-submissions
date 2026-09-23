class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for n in nums:
            two, one = one, max(one, n + two)
        return one
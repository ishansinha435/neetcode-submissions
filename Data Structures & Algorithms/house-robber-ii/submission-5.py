class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.sub_rob(nums[1:]), self.sub_rob(nums[:-1])) if len(nums) > 1 else nums[0]
        
    def sub_rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for n in nums:
            two, one = one, max(one, n + two)
        return one
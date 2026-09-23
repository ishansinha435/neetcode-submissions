class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.sub_rob(nums[1:]), self.sub_rob(nums[:-1]))
        
    def sub_rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for n in nums:
            two, one = one, max(one, n + two)
        return one
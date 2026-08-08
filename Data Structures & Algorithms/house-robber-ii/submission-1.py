class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        def helper(l, r):
            one, two = 0, 0
            for i in range(l, r):
                temp = max(nums[i] + one, two)
                one = two
                two = temp
            return two
        
        return max(helper(0, len(nums) - 1), helper(1, len(nums)))
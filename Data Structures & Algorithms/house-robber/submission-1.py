class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        one, two = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums), 2):
            one = max(nums[i] + one, two)
            two = max(nums[i + 1] + two, one) if i + 1 < len(nums) else two

        return max(one, two)
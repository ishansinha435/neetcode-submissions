class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if i != 0 and n == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                curr_sum = n + nums[j] + nums[k]
                if curr_sum < 0:
                    j += 1
                elif curr_sum > 0: 
                    k -= 1
                else:
                    res.append([n, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return res
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if n > 0:
                break
            if not i == 0 and nums[i - 1] == n:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr = n + nums[l] + nums[r]
                if curr < 0:
                    l += 1
                elif curr > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res
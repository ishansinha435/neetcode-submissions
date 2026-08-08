class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, hset = 0, set()
        for r, n in enumerate(nums):
            if n in hset:
                continue
            hset.add(n)
            nums[l] = n
            l += 1
        return l

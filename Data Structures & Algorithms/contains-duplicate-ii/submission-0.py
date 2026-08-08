class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}
        for i, n in enumerate(nums):
            if n in hmap and i - hmap[n] <= k:
                return True
            hmap[n] = i
        return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
            if hashmap[n] > 1: return True
        return False
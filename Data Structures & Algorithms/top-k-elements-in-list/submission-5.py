class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap, res = {}, []
        for n in nums:
            hmap[n] = 1 + hmap.get(n, 0)
        counts = [[] for _ in range(len(nums) + 1)]
        for n, c in hmap.items():
            counts[c].append(n)
        for i in range(len(counts) - 1, -1 , -1):
            for n in counts[i]:
                res.append(n)
            if len(res) == k:
                return res

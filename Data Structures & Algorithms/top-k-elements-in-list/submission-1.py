class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for n in nums:
            hmap[n] = 1 + hmap.get(n, 0)
        buckets = [[] for _ in range(len(nums) + 1)]
        for key in hmap:
            buckets[hmap[key]].append(key)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
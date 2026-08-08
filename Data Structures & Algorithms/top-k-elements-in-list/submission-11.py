class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res, buckets = [], [[] for _ in range(len(nums) + 1)]
        for n, c in counts.items():
            buckets[c].append(n)
        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
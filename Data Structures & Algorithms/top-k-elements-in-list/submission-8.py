class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts, buckets = {}, [[] for _ in range(len(nums) + 1)]
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        for num, count in counts.items():
            buckets[count].append(num)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
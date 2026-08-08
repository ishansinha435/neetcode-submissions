class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        res, hmap = [], defaultdict(list)
        for idx, score in items:
            hmap[idx].append(score)
        for idx, scores in hmap.items():
            heapq.heapify_max(scores)
            avg = sum(heapq.heappop_max(scores) for _ in range(5)) // 5
            res.append([idx, avg])
        res.sort()
        return res

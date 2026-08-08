class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap, hmap = [], defaultdict(list)
        for x, y in points:
            dist = math.sqrt(x ** 2 + y ** 2)
            if dist not in hmap:
                heapq.heappush(heap, dist)
            hmap[dist].append((x, y))
        res = []
        while True:
            dist_list = hmap[heapq.heappop(heap)]
            for x, y in dist_list:
                res.append([x, y])
            if len(res) == k: 
                break
        return res
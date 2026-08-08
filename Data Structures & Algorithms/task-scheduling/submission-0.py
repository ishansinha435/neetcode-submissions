class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res, heap, q, hmap = 0, [], deque(), defaultdict(int)
        for t in tasks:
            hmap[t] -= 1
        for v in hmap.values():
            heapq.heappush(heap, v)
        while heap or q:
            if heap:
                largest = 1 + heapq.heappop(heap)
                if largest != 0:
                    q.append((largest, res + n + 1))
            res += 1
            if q and q[0][1] == res:
                heapq.heappush(heap, q.popleft()[0])
        return res

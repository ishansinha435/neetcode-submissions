class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        for _ in range(k):
            pile = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts, floor(sqrt(pile)))
        return sum(gifts)
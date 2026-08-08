class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.largest = nums
        self.k = k

    def add(self, val: int) -> int:
        if len(self.largest) < self.k:
            heapq.heappush(self.largest, val)
        elif val > self.largest[0]:
            heapq.heappushpop(self.largest, val)
        return self.largest[0]

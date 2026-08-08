class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, q = [], deque()
        for i in range(k):
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
        res.append(q[0])
        l = 0
        for r in range(k, len(nums)):
            if nums[l] == q[0]:
                q.popleft()
            l += 1
            while q and nums[r] > q[-1]:
                q.pop()
            q.append(nums[r])
            res.append(q[0])
        return res

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, res = deque(), []
        for i in range(k):
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
        res.append(q[0])
        l = 0
        for i in range(k, len(nums)):
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
            if nums[l] == q[0]:
                q.popleft()
            l += 1
            res.append(q[0])
        return res
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = deque([[]])

        def dfs(i):
            nonlocal res
            if i == len(nums):
                return
            dfs(i + 1)
            for j in range(len(res)):
                arr = res.popleft()
                for k in range(len(arr) + 1):
                    copy = arr.copy()
                    copy.insert(k, nums[i])
                    res.append(copy)

        dfs(0)
        return list(res)
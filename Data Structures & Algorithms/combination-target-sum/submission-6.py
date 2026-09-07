class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i, arr, total):
            if i == len(nums) or total > target:
                return
            if total == target:
                res.append(arr.copy())
                return
            arr.append(nums[i])
            backtrack(i, arr, total + nums[i])
            arr.pop()
            backtrack(i + 1, arr, total)

        backtrack(0, [], 0)
        return res
            
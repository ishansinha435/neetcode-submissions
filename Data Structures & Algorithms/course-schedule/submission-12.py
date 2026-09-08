class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap = defaultdict(list)
        for course, pre in prerequisites:
            hmap[course].append(pre)
        visited = set()
        memo = {}

        def dfs(course):
            if course in memo:
                return memo[course]
            if course in visited:
                return False
            visited.add(course)
            res = True
            for c in hmap[course]:
                if not dfs(c):
                    res = False
                    break
            visited.remove(course)
            memo[course] = res
            return res

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap = {i : [] for i in range(numCourses)}
        for course, pre in prerequisites:
            hmap[course].append(pre) 
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            visited.add(course)
            for pre in hmap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            return True

        for course in hmap:
            if not dfs(course):
                return False
        return True

            
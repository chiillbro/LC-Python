class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i : [] for i in range(numCourses)}

        for crs, prereq in prerequisites:
            prereq_map[crs].append(prereq)
        
        visited = [False] * numCourses
        onStack = [False] * numCourses
        res = []

        def dfs(crs):
            visited[crs] = True
            onStack[crs] = True

            for pre in prereq_map[crs]:
                if not visited[pre]:
                    if not dfs(pre):
                        return False
                elif onStack[pre]:
                    return False
            
            res.append(crs)
            onStack[crs] = False
            return True
        

        for crs in range(numCourses):
            if not visited[crs]:
                if not dfs(crs):
                    return []
        
        return res
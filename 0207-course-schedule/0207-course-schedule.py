class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crs_preq_map = {i : [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            crs_preq_map[crs].append(prereq)

        # ** Topological Sort ** #
        
        visited = [False] * numCourses
        cycle = [False] * numCourses
        # def dfs(crs):
        #     if crs in visited:
        #         return False
        #     if not crs_preq_map[crs]: return True
        #     visited.add(crs)
        #     for prereq in crs_preq_map[crs]:
        #         if not dfs(prereq): return False
        #     visited.remove(crs)
        #     crs_preq_map[crs] = []
        #     return True

        def dfs(crs):
            visited[crs] = True
            cycle[crs] = True
            for neigh in crs_preq_map[crs]:
                if not visited[neigh]:
                    if not dfs(neigh):
                        return False
                elif cycle[neigh]:
                    return False
            
            cycle[crs] = False
            return True

        for crs in crs_preq_map:
            if not dfs(crs): return False
            
        return True
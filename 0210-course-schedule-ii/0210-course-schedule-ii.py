class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i : [] for i in range(numCourses)}

        for prereq, crs in prerequisites:
            prereq_map[prereq].append(crs)
        
        visited_and_cycle = [[False, False] for _ in range(numCourses)]
        res = []

        def dfs(crs):
            visited_and_cycle[crs] = [True, True]
            for pre in prereq_map[crs]:
                if not visited_and_cycle[pre][0]:
                    if not dfs(pre):
                        return False
                elif visited_and_cycle[pre][1]:
                    return False
            
            res.append(crs)
            visited_and_cycle[crs][1] = False
            return True
        

        for crs in range(numCourses):
            if not visited_and_cycle[crs][0]:
                if not dfs(crs):
                    return []
        
        return res
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crs_preq_map = {i : [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            crs_preq_map[crs].append(prereq)

        # ** Topological Sort ** #
        
        visited = [False] * numCourses
        cycle = [False] * numCourses

        # ** Using only one visited array ** #

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

        # ** using two arrays to keep track of visited and cycle ** #
        # def dfs(crs):
        #     visited[crs] = True
        #     cycle[crs] = True
        #     for neigh in crs_preq_map[crs]:
        #         if not visited[neigh]:
        #             if not dfs(neigh):
        #                 return False
        #         elif cycle[neigh]:
        #             return False
            
        #     cycle[crs] = False
        #     return True

        # for crs in crs_preq_map:
        #     if not dfs(crs): return False

        # return True


        # ** Kahn's Algorithm or BFS ** #

        in_degree = [0] * numCourses

        for neighs in crs_preq_map.values():
            for neigh in neighs:
                in_degree[neigh] += 1
        
        queue = deque([node for node, degree in enumerate(in_degree) if not degree])

        topo_count = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                topo_count += 1
                for neigh in crs_preq_map[cur]:
                    in_degree[neigh] -= 1
                    if not in_degree[neigh]:
                        queue.append(neigh)
        
        return topo_count == numCourses
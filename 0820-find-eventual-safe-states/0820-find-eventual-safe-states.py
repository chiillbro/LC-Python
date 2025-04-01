class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        
        # ** reverse graph + Kahn's Algorithm (BFS-based Topological sort) ** #

        # rev_graph = [[] for _ in range(V)]

        # in_degree = [0] * V
        # for i in range(V):
        #     for neigh in graph[i]:
        #         rev_graph[neigh].append(i)
        #         in_degree[i] += 1
        
        # queue = deque([node for node, degree in enumerate(in_degree) if not degree])

        # safe_nodes = []
        # while queue:
        #     for _ in range(len(queue)):
        #         cur = queue.popleft()
        #         safe_nodes.append(cur)
        #         for neigh in rev_graph[cur]:
        #             in_degree[neigh] -= 1
        #             if not in_degree[neigh]:
        #                 queue.append(neigh)
        
        # return sorted(safe_nodes)


        # ** DFS based cycle detection Algorithm *8 #
        visited = [False] * V
        cycle = [False] * V
        safe_nodes = []
        def dfs(node):
            visited[node] = True
            cycle[node] = True

            for neigh in graph[node]:
                if not visited[neigh]:
                    if not dfs(neigh):
                        return False
                elif cycle[neigh]:
                    return False
            
            safe_nodes.append(node)
            cycle[node] = False
            return True

        for node in range(V):
            if not visited[node]:
                dfs(node)

        return sorted(safe_nodes)

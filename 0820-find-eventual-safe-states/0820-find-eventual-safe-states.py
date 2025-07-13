class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        v = len(graph)

        adj_list = defaultdict(list)

        in_degree = [0] * v

        for node in range(v):
            in_degree[node] = len(graph[node])
            for neigh in graph[node]:
                adj_list[neigh].append(node)
        
        queue = deque()

        for node, cnt in enumerate(in_degree):
            if cnt == 0:
                queue.append(node)
            

        topo = []

        while queue:
            cur = queue.popleft()
            topo.append(cur)
            for neigh in adj_list[cur]:
                in_degree[neigh] -= 1

                if in_degree[neigh] == 0:
                    queue.append(neigh)

        topo.sort()

        return topo

        # visited, on_stack = [0] * v, [0] * v

        # safe_states = [0] * v

        # def dfs(cur):
        #     visited[cur] = 1

        #     on_stack[cur] = 1
        #     safe_state = True
        #     for neigh in graph[cur]:
        #         if not visited[neigh]:
        #             if dfs(neigh):
        #                 return True

        #         elif on_stack[neigh]:
        #             return True
            
        #     on_stack[cur] = 0
        #     safe_states[cur] = 1
        #     return False
        
        # for i in range(v):
        #     if not visited[i]:
        #         dfs(i)
        

        # return [i for i, v in enumerate(safe_states) if v]
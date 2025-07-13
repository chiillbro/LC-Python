class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        v = len(graph)


        visited, on_stack = [0] * v, [0] * v

        safe_states = [0] * v

        def dfs(cur):
            visited[cur] = 1

            on_stack[cur] = 1
            safe_state = True
            for neigh in graph[cur]:
                if not visited[neigh]:
                    if dfs(neigh):
                        return True

                elif on_stack[neigh]:
                    return True
            
            on_stack[cur] = 0
            safe_states[cur] = 1
            return False
        
        for i in range(v):
            if not visited[i]:
                dfs(i)
        

        return [i for i, v in enumerate(safe_states) if v]
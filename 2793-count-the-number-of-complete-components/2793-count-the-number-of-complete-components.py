class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # ** Approach 1 : Adjacency List **
        # graph = [[vertex] for vertex in range(n)]
        # adjacency_list = defaultdict(int)

        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)
        

        # for vertex in range(n):
        #     neighbors = tuple(sorted(graph[vertex]))
        #     adjacency_list[neighbors] += 1
        

        # return sum(
        #     1 for neighbors, freq in adjacency_list.items()
        #     if len(neighbors) == freq
        # )



        # ** Approach 2 : Traditional Graph techniques DFS **

        # adjacency_list = defaultdict(list)

        # for u, v in edges:
        #     adjacency_list[u].append(v)
        #     adjacency_list[v].append(u)
        
        # visited = set()
        # complete_count = 0

        # def _dfs(curr : int, info : List[int]):
        #     visited.add(curr)
        #     info[0] += 1
        #     info[1] += len(adjacency_list[curr])

        #     for neighbor in adjacency_list[curr]:
        #         if neighbor not in visited:
        #             _dfs(neighbor, info)
        

        # for vertex in range(n):
        #     if vertex not in visited:
        #         info = [0, 0]
        #         _dfs(vertex, info)

        #         if info[0] * (info[0] - 1) == info[1]:
        #             complete_count += 1
            
        # return complete_count



        # ** Approach 3 : Traditional Graph techniques BFS **
        
        adjacency_list = defaultdict(list)

        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        
        visited, complete_count = set(), 0

        for vertex in range(n):
            if vertex in visited:
                continue
            
            component = []
            queue = deque([vertex])
            visited.add(vertex)

            while queue:
                curr = queue.popleft()
                component.append(curr)

                for neighbor in adjacency_list[curr]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                
            is_complete = True
            for node in component:
                if len(adjacency_list[node]) != len(component) - 1:
                    is_complete = False
                    break
            
            complete_count += 1 if is_complete else 0

        return complete_count
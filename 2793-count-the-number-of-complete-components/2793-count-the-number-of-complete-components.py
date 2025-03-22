class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = [[vertex] for vertex in range(n)]
        adjacency_list = defaultdict(int)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        

        for vertex in range(n):
            neighbors = tuple(sorted(graph[vertex]))
            adjacency_list[neighbors] += 1
        

        return sum(
            1 for neighbors, freq in adjacency_list.items()
            if len(neighbors) == freq
        )
        
        
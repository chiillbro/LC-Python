class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj_list = defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            adj_list[u].append(v)
            in_degree[v] += 1


        dp = [[0] * 26 for _ in range(n)]

        q = deque()
        for i in range(n):
            if not in_degree[i]:
                q.append(i)
                dp[i][ord(colors[i]) - 97] += 1
        
        visited, res = 0, 0
        while q:
            u = q.popleft()
            visited += 1
            res = max(res, max(dp[u]))

            for v in adj_list[u]:
                ci = ord(colors[v]) - 97
                for c in range(26):
                    val = dp[u][c] + (1 if c == ci else 0)
                    if val > dp[v][c]:
                        dp[v][c] = val
                    
                in_degree[v] -= 1
                if not in_degree[v]:
                    q.append(v)
        
        return res if visited == n else -1
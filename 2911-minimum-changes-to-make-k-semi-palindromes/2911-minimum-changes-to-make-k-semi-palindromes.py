class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float("inf")
        def palindrome_cost(g):
            i = 0
            j = len(g) - 1
            cost = 0
            while i < j:
                if g[i] != g[j]:
                    cost += 1
                
                i += 1
                j -= 1
            
            return cost
        
        cost = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            cost[i][i] = INF
        

        for i in range(n):
            for j in range(i+1, n):
                sub_string = s[i:j+1]
                L = len(sub_string)
                min_cost = INF
                for d in range(1, L):
                    if L % d == 0:
                        d_cost = 0
                        for g in range(d):
                            d_cost += palindrome_cost(sub_string[g::d])
                
                        min_cost = min(min_cost, d_cost)
                
                cost[i][j] = min_cost
        

        dp = [[INF for _ in range(k+1)] for _ in range(n+1)]
        dp[0][0] = 0
        
        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = min(dp[m][j-1] + cost[m][i-1] for m in range(i))
        

        return dp[-1][-1]
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        ans = sum(fruits[i][i] for i in range(n)) # first child's optimal path would be the diagnol

        def dp():
            prev = [0] * (n)
            cur = [0] * (n)

            prev[n-1] = fruits[0][n-1]

            for i in range(1, n-1):
                for j in range(max(n-1-i, i+1), n): # avoiding the diagnol (already claimed by first child)

                    # as per problem statement, second child's movements
                    
                    # 1. directly below
                    best = prev[j]

                    # 2. left to the directly below
                    if j-1 >= 0:
                        best = max(best, prev[j-1])
                    
                    # 3. right to the directly below
                    if j+1 < n:
                        best = max(best, prev[j+1])
                    
                    cur[j] = best + fruits[i][j]

                    # above we did it in reverse, for every room, the source room would exactly those rooms from the directions mentioned above
                    # so, we are picking the optimal source room for every room
                
                prev, cur = cur, prev
            
            return prev[n-1]

        
        ans += dp() # second child's contribution

        # third child's traversal from bottom-left to bottom-right is a mirror of the second child’s path across the diagnol, so, if we do "matrix transpose" the bottom-left part to top-right and we can simply use the dp we wrote above as the third child also now has the same directions

        for i in range(n):
            for j in range(i):
                fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]
        
        ans += dp() # third child's contribution

        return ans
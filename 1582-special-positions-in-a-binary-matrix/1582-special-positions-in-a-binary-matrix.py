class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])

        def check(row, col):
            for c in range(m):
                if c == col: continue
                
                if mat[row][c] == 1:
                    return False
                
            for r in range(n):
                if r == row:
                    continue
                
                if mat[r][col] == 1:
                    return False
                
            
            return True

        res = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and check(i, j):
                    res += 1
        

        return res

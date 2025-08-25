class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        res = []

        def helper(i, j, dir):
            cur = []
            while i < n and j >= 0:
                cur.append(mat[i][j])
                i += 1
                j -= 1
            if dir:
                res.extend(cur)
            else:
                cur.reverse()
                res.extend(cur)
        
        dir = 0
        for i in range(m):
            helper(0, i, dir)
            dir = 1 - dir
        
        for j in range(1, n):
            helper(j, m-1, dir)
            dir = 1 - dir
        
        return res
            

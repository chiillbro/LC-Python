class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            cur = [1]
            for j in range(1, i):
                first = res[-1][j-1]
                second = res[-1][j]
                cur.append(first + second)
            cur.append(1)
            res.append(cur)
    
        return res
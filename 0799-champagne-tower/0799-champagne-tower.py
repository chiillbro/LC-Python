class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * x for x in range(1, 102)]

        tower[0][0] = poured

        for i in range(query_row+1):
            for j in range(i+1):
                q = (tower[i][j] - 1.0) / 2.0

                if q > 0:
                    tower[i+1][j] += q
                    tower[i+1][j+1] += q

        

        return min(1, tower[query_row][query_glass])
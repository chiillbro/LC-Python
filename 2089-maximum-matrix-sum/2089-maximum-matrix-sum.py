class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        neg_count = 0
        min_val = inf

        total = 0
        for row in range(n):
            for col in range(n):
                cur = matrix[row][col]
                if cur <= 0:
                    neg_count += 1
                min_val = min(abs(cur), min_val)
                total += abs(cur)
        
        if neg_count & 1:
            return total - min_val * 2
        
        return total
                

                
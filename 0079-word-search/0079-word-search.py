class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        N = len(word)
        visited = set()
        def backtrack(row, col, cur):
            if cur == N:
                return True
            
            if not (0 <= row < m) or not (0 <= col < n) or (row, col) in visited or board[row][col] != word[cur]: return False
            
            visited.add((row, col))

            res = backtrack(row + 1, col, cur + 1) or backtrack(row - 1, col, cur + 1) or backtrack(row, col + 1, cur + 1) or backtrack(row, col - 1, cur + 1)
            
            visited.remove((row, col))
            
            return res
        
        count = Counter(word)

        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        
        for r in range(m):
            for c in range(n):
                if backtrack(r, c, 0): return True

        return False
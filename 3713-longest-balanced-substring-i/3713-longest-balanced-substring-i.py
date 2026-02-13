class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        res = 0

        for i in range(n):
            if res >= n - i:
                break
            cur = defaultdict(int)
            for j in range(i, n):
                char = s[j]

                cur[char] += 1
                
                if len(set(cur.values())) == 1:
                    res = max(res, j - i + 1)
        
        return res

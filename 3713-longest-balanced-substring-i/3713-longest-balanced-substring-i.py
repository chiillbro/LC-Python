class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        seen = [0] * 26

        res = 0

        for i in range(n):
            if res >= n - i:
                break
            cur = defaultdict(int)
            for j in range(i, n):
                char = s[j]
                char_val = ord(char) - 97

                # if seen[char_val] != :
                cur[char_val] += 1
                # seen[char_val] = i + 1
                
                if len(set(cur.values())) == 1:
                    res = max(res, j - i + 1)
        
        return res

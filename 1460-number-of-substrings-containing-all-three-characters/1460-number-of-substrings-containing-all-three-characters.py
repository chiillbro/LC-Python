class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        res = l = 0
        count_map = defaultdict(int)

        for r in range(N):
            count_map[s[r]] += 1

            while len(count_map) == 3:
                res += N - r
                count_map[s[l]] -= 1
                if count_map[s[l]] == 0:
                    count_map.pop(s[l])
                l += 1
        
        return res        
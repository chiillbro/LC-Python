class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        res = 0

        for i in range(n):
            if res >= n - i:
                break
            # cur = defaultdict(int)
            freq = [0] * 26
            dist  = 0
            max_f = 0
            cnt = 1
            for j in range(i, n):
                char = s[j]
                char_val = ord(char) - 97

                dist += freq[char_val] == 0

                freq[char_val] += 1
                max_f = max(max_f, freq[char_val])

                if dist * max_f == cnt:
                    res = max(res, cnt)
                
                cnt += 1

                # cur[char] += 1
                
                # if len(set(cur.values())) == 1:
                #     res = max(res, j - i + 1)
        
        return res

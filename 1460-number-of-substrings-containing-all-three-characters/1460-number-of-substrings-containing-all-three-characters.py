class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # using Sliding Window Approach

        n = len(s)

        # freq_map = defaultdict(int)
        # left = res = 0

        # for right in range(n):
        #     freq_map[s[right]] += 1

        #     while len(freq_map) == 3:
        #         res += n - right
        #         freq_map[s[left]] -= 1
        #         if not freq_map[s[left]]:
        #             freq_map.pop(s[left])
                
        #         left += 1

        # Last Position Tracking Approach

        last = [-1] * 3

        res = 0
        
        for i, char in enumerate(s):
            last[ord(char) - ord('a')] = i

            res += 1 + min(last)
            
        return res
class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        N = len(s)

        for i in range(N - 1):
            freq = defaultdict(int)
            freq[s[i]] += 1
            for j in range(i+1, N):
                freq[s[j]] += 1
                res += max(freq.values()) - min(freq.values())
        
        return res

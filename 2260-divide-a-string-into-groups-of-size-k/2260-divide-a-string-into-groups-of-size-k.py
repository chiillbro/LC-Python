class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        res = []

        for i in range(0, n, k):
            if i + k <= n:
                res.append(s[i:i+k])
        
        if i + k == n:
            return res
        elif i + k > n:
            rem = k - (n - i)
            res.append(s[i:] + fill * rem)
        
        return res
from math import factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        unique = set()

        base = 10 ** ((n-1) >> 1)
        skip = n & 1

        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]

            palidromicInt = int(s)

            if not (palidromicInt % k):
                sorted_s = "".join(sorted(s))
                unique.add(sorted_s)
        

        fac = [factorial(i) for i in range(n + 1)]
        ans = 0

        for s in unique:
            cnt = [0] * 10
            for c in s:
                cnt[int(c)] += 1
            
            tot = (n - cnt[0]) * fac[n-1]
            for x in cnt:
                tot //= fac[x]
            
            ans += tot
        
        return ans
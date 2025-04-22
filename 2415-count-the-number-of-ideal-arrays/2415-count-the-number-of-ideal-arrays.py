# ** prime‐factor + stars‑and‑bars solution ** #

MOD = 10 ** 9 + 7
MAX_N = 10 ** 4 + 10

# MAX_P is chosen to exceed the maximum possible exponent E of any prime in any x≤10^4
 
# The worst case is 2^13 = 8192 (exponent 13), and 2^14 = 16384 exceeds 10000, so no exponent >13 occurs.
# We round up to 15 for safety.
# This bounds how large each Ei can be, so we know how big our combination table needs to be in the second dimension

MAX_P = 15

# Precomputing Prime‐Factor Exponents (ps[x]) via a Sieve
sieve = [0] * MAX_N

for i in range(2, MAX_N):
    if not sieve[i]:
        for j in range(i, MAX_N, i):
            sieve[j] = i


# Factor out each x into exponents
ps = [[] for _ in range(MAX_N)]

for i in range(2, MAX_N):
    x = i
    while x > 1:
        p = sieve[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        ps[i].append(cnt)

# After this, ps[x] is the list [E1, E2, ...]


# Precomputing Combinations (i / j)

# We need to compute 
# (n + E - 1) / E for 0 ≤ E ≤15 and 0≤\U0001d45b+\U0001d438−1≤10^4+15 and 0 ≤ n+E−1 ≤ 10^4 + 15. We build Pascal’s triangle up to those limits

C = [[0] * (MAX_P + 1) for _ in range(MAX_N + MAX_P)]
C[0][0] = 1

for i in range(1, MAX_N + MAX_P):
    C[i][0] = 1
    for j in range(1, min(i, MAX_P) + 1):
        C[i][j] = (C[i - 1][j] + C[i-1][j-1]) % MOD


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = 0

        for x in range(1, maxValue + 1):
            ways = 1
            # for each prime‐exponent E in x:
            for E in ps[x]:  
                ways = ways * C[n + E - 1][E] % MOD
            ans = (ans + ways) % MOD
        return ans
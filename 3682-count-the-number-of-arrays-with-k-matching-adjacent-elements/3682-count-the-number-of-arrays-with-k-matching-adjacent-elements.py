MOD = 10**9 + 7
maxN = 100000

fact = [1] * (maxN + 1)
inv_fact = [1] * (maxN + 1)

for i in range(1, maxN + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact[maxN] = pow(fact[maxN], MOD - 2, MOD)
for i in range(maxN, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % MOD



def qpow(x, n):
    res = 1
    while n:
        if n & 1:
            res = res * x % MOD
        x = x * x % MOD
        n >>= 1
    return res


def init():
    if fact[0] != 0:
        return
    fact[0] = 1
    for i in range(1, MX):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[MX - 1] = qpow(fact[MX - 1], MOD - 2)
    for i in range(MX - 1, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD


def comb(n, m):
    return fact[n] * inv_fact[m] % MOD * inv_fact[n - m] % MOD


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        d = n - k
        if d < 1:
            return 0
        term1 = m * pow(m - 1, d - 1, MOD) % MOD
        num = n - 1
        den1 = d - 1
        den2 = k
        if den1 < 0 or den2 < 0:
            binom_val = 0
        else:
            binom_val = fact[num] * inv_fact[den1] % MOD
            binom_val = binom_val * inv_fact[den2] % MOD
        return term1 * binom_val % MOD
def count_fixed_length(L, k, bound_str):
    if bound_str is None:
        bound_str = '9' * L
    weight = [0] * L
    base = 1
    for i in range(L-1, -1, -1):
        weight[i] = base
        base = (base * 10) % k

    dp = [[[0] * (L+1) for _ in range(k)] for _ in range(2)]
    first_digit = int(bound_str[0])
    for d in range(1, first_digit+1):
        tight_next = 1 if d == first_digit else 0
        mod_val = (d * weight[0]) % k
        ec = 1 if d % 2 == 0 else 0
        dp[tight_next][mod_val][ec] += 1

    for pos in range(1, L):
        new_dp = [[[0] * (L+1) for _ in range(k)] for _ in range(2)]
        for tight in range(2):
            for mod_val in range(k):
                for ec_count in range(L+1):
                    count_here = dp[tight][mod_val][ec_count]
                    if count_here == 0:
                        continue
                    current_bound = int(bound_str[pos]) if tight else 9
                    for d in range(0, current_bound+1):
                        new_tight = tight and (d == current_bound)
                        new_mod = (mod_val + d * weight[pos]) % k
                        new_ec = ec_count + (1 if d % 2 == 0 else 0)
                        if new_ec > L:
                            continue
                        new_dp[new_tight][new_mod][new_ec] += count_here
        dp = new_dp

    total = 0
    for tight in range(2):
        for mod_val in range(k):
            for ec_count in range(L+1):
                if ec_count == L // 2 and mod_val % k == 0:
                    total += dp[tight][mod_val][ec_count]
    return total

def count_up_to(n, k):
    if n < 10:
        return 0
    s = str(n)
    total_digits = len(s)
    total_count = 0
    for L in range(2, total_digits+1, 2):
        if L < total_digits:
            total_count += count_fixed_length(L, k, None)
        else:
            total_count += count_fixed_length(L, k, s)
    return total_count

class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        return count_up_to(high, k) - count_up_to(low-1, k)
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        powers = []

        bin_repr = bin(n)

        j = 0
        for i in range(len(bin_repr)-1, 1, -1):
            if bin_repr[i] == "1":
                powers.append(1 << j)
            
            j += 1

        prod_arr = [1] * (len(powers))
        prod_arr[0] = powers[0]

        for i in range(1, len(powers)):
            prod_arr[i] = prod_arr[i-1] * powers[i]
        
        ans = []

        for l, r in queries:
            cur = 1

            if l == 0:
                cur = prod_arr[r] % MOD
            else:
                cur = prod_arr[r] // prod_arr[l-1] % MOD
            
            ans.append(cur)
        
        return ans

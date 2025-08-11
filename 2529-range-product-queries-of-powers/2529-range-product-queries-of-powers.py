class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        powers = []

        # bin_repr = bin(n)

        # j = 0
        # for i in range(len(bin_repr)-1, 1, -1):
        #     if bin_repr[i] == "1":
        #         powers.append(1 << j)
            
        #     j += 1

        for i in range(30):
            if (n >> i) & 1:
                powers.append(1 << i)

        prod_arr = [1] * (len(powers))
        prod_arr[0] = powers[0] % MOD

        for i in range(1, len(powers)):
            prod_arr[i] = (prod_arr[i-1] * powers[i]) % MOD
        
        ans = []

        for l, r in queries:
            product_up_to_r = prod_arr[r]

            if l == 0:
                ans.append(product_up_to_r)
            else:
                product_up_to_l_minus_1 = prod_arr[l-1]
                mod_inverse = pow(product_up_to_l_minus_1, MOD - 2, MOD)
                # cur = prod_arr[r] // prod_arr[l-1]
                cur = (product_up_to_r * mod_inverse) % MOD
                
                ans.append(cur)
        
        return ans

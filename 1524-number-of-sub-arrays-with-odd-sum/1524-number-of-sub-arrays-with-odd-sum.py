class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n = len(arr)

        count_even, count_odd = 1, 0
        ans = 0
        pref_parity = 0

        for num in arr:
            pref_parity += num

            if (pref_parity & 1) != 0:
                ans += count_even
                count_odd += 1
            else:
                ans += count_odd
                count_even += 1
        
        return ans % (10**9 + 7)
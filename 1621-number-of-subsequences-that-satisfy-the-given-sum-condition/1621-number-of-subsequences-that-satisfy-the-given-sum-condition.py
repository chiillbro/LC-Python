class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()

        res = 0
        # for i in range(n):
        #     if nums[i] > target:
        #         continue
        #     for j in range(i, n):
        #         if nums[i] + nums[j] <= target:
        #             res += (1 << (j - i - 1) if i != j else 1)
        #             res %= MOD
        #         else:
        #             break
    
        # The above approve gives TLE, so if we observe something, at every range i...j, we are just caring about min and max elements which are exactly nums[i] and nums[j] since we already sorted the array
        # And since the max element in the i...j range forms sum <= target, then every element to the left of jth idx can contribute to subsequences, so 
        # We already know, if there are 4 elements, the total no.of subsequences can be formed are 2^n (including a empty sub sequence)

        # now, we can use this formula
        # problem already stated that we should include only non-empty sequence
        # Now, we can use a two pointer approach, one pointing at start and one at end and depending on the current min max sum, we will shrink or update our result to add contributing sequence couns

        i, j = 0, n-1

        while i <= j:
            _sum = nums[i] + nums[j]
            if _sum <= target:
                res += (1 << (j-i))
                res %= MOD
                i += 1
            else:
                j -= 1

        return res
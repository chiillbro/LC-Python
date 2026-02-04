class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 4: return 0

        ans = -inf
        i = 0

        while i < n:
            j = i + 1
            res = 0
            while j < n and nums[j] > nums[j-1]:
                j += 1
            
            p = j - 1

            if p == i:
                i += 1
                continue
        
            res += nums[p] + nums[p-1]

            while j < n and nums[j] < nums[j-1]:
                res += nums[j]
                j += 1
            
            q = j - 1

            if p == q or q == n - 1 or (j < n and nums[j] == nums[q]):
                i = q
                continue
            
            res += nums[q + 1]

            max_sum = 0
            cur_sum = 0
            k = q + 2
            while k < n and nums[k] > nums[k-1]:
                cur_sum += nums[k]
                max_sum = max(cur_sum, max_sum)
            
                k += 1
            
            res += max_sum


            max_sum = 0
            cur_sum = 0
            
            for l in range(p-2, i - 1, -1):
                cur_sum += nums[l]
                max_sum = max(cur_sum, max_sum)
            
            res += max_sum

            ans = max(ans, res)
            i = q

        return ans
            

        # inc1 = [-inf] * n

        # inc1[0] = nums[0]

        # dec = [-inf] * n
        
        # inc2 = [-inf] * n

        # for i in range(1, n):
        #     if nums[i] > nums[i-1]:
        #         inc1[i] = max(nums[i], inc1[i-1] + nums[i])
        #     else:
        #         inc1[i] = nums[i]

        #     if nums[i] < nums[i-1]:
        #         dec[i] = max(dec[i-1], inc1[i-1]) + nums[i]

            
        #     if nums[i] > nums[i-1]:
        #         inc2[i] = max(inc2[i-1], dec[i-1]) + nums[i]


        
        # return max(inc2) if max(inc2) != -inf else 0

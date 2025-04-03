class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)

        # ** Greedy + Prefix Suffix Array ** TC: O(n), SC: O(n) #

        # left_max = [0] * n
        # right_max = [0] * n

        # for i in range(1, n):
        #     left_max[i] = max(left_max[i-1], nums[i-1])
        #     right_max[n - 1 - i] = max(right_max[n - i], nums[n - i])
        
        # res = 0
        # for j in range(1, n-1):
        #     res = max(res, (left_max[j] - nums[j]) * right_max[j])
        
        # return res


        # ** Greedy ** TC: O(n), SC: O(1) #

        res = i_max = d_max = 0

        for k in range(n):
            res = max(res, d_max * nums[k])
            d_max = max(d_max, i_max - nums[k])
            i_max = max(i_max, nums[k])
        
        return res




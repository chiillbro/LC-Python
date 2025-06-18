class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # nums: []int, size is multiple of 3
        # k: int, positive integer

        # return 2d array of size 3 arrays with mentioned conditions

        n = len(nums)
        ans = []

        # sorting the array helps I think

        nums.sort()

        # num_arrays = n // 3

        i = 0
        while i <= n-3:
            num1, num2, num3 = nums[i], nums[i+1], nums[i+2]
            if num2 - num1 > k or num3 - num2 > k or num3 - num1 > k:
                return []
            
            ans.append([num1, num2, num3])
            i += 3
        
        return ans



        return ans



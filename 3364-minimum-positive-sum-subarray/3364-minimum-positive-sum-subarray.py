class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n+1)

        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        

        res = float("inf")
        for length in range(l, r+1):
            for start in range(n+1-length):
                sub_sum = prefix_sum[start+length] - prefix_sum[start]
                if sub_sum > 0:
                    res = min(res, sub_sum)

        
        return -1 if res == float("inf") else res

    
    # nums = [3, -2, 1, 4]
    # prefix_sum = [0, 3, 1, 2, 6]
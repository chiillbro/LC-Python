class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n+1)

        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        

        res = float("inf")
        # for length in range(l, r+1):
        #     for start in range(n+1-length):
        #         sub_sum = prefix_sum[start+length] - prefix_sum[start]
        #         if sub_sum > 0:
        #             res = min(res, sub_sum)


        # ** O(n logn) approach using Python's SortedList data structure

        window = SortedList()
        for j in range(l, n+1):
            window.add(prefix_sum[j-l])

            if j-r-1 >= 0:
                window.remove(prefix_sum[j-r-1])
            
            idx = window.bisect_left(prefix_sum[j]) - 1

            if idx >= 0:
                res = min(res, prefix_sum[j] - window[idx])
        
        return -1 if res == float("inf") else res

    
    # nums = [3, -2, 1, 4]
    # prefix_sum = [0, 3, 1, 2, 6]
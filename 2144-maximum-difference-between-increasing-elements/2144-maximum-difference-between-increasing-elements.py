class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # nums: int[]
        # Brute force:
        n = len(nums)

        # _max_diff = -1
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[j] > nums[i]:
        #             _max_diff = max(_max_diff, nums[j] - nums[i])
    
        # return _max_diff


        # now, the question is how to optimize this

        # okay, I've thought of a different approach, this approach solves the problem in O(n) but consumes O(n) space, let's see


        # suffix_max = [0] * n
        # suffix_max[n-1] = nums[-1]

        # for i in range(n-2, -1, -1):
        #     suffix_max[i] = max(suffix_max[i+1], nums[i])
        
        # _max_diff = -1

        # for i in range(n-1):
        #     if suffix_max[i+1] > nums[i]:
        #         _max_diff = max(_max_diff, suffix_max[i+1] - nums[i])
    
        # return _max_diff


        # okay, the above approach is not bad, but I've got the optimal solution from the editorial which I think is actually clever (and somewhat resembles Boyer's Moore voting algorithm)

        prev_min = nums[0]

        _max_diff = -1

        for i in range(1, n):
            if nums[i] > prev_min:
                _max_diff = max(_max_diff, nums[i] - prev_min)
            else:
                prev_min = nums[i]

        return _max_diff



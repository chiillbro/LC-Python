class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        # ** Brute Force : TLE error **
        # track_map = {i : v for i, v in enumerate(nums) if v != 0}
        # res = 0

        # for l, r, v in queries:
        #     if not track_map:
        #         return res
        #     for i in range(l, r + 1):
        #         if i in track_map:
        #             track_map[i] -= min(track_map[i], v)
        #             if track_map[i] == 0:
        #                 track_map.pop(i)
            
        #     res += 1
        
        # return -1 if track_map else res

        # ** Second Approach Binary Search and Difference Array **
        left, right = 0, len(queries)
        if not self.canFormZeroArray(nums, queries, right):
            return -1
        
        while left <= right:
            mid = left + (right - left) // 2

            if self.canFormZeroArray(nums, queries, mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left

    def canFormZeroArray(self, nums, queries, k):
        N = len(nums)
        total_sum = 0
        difference_sum = [0] * (N + 1)

        for query_idx in range(k):
            l, r, v = queries[query_idx]
            difference_sum[l] += v
            difference_sum[r+1] -= v
        
        for num_idx in range(N):
            total_sum += difference_sum[num_idx]
            if total_sum < nums[num_idx]:
                return False
        return True



class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # nums: int[], eg: [10, 1, 2, 7, 1, 3]
        # p: int
        n = len(nums)

        # [3, 4, 2, 3, 2, 1, 2]

        if not p:
            return 0


        # sorting helps, cause the difference between two elements is the max minimum that we can get if we consider adjacent elements in the sorted array

        nums.sort()
        # [1, 2, 2, 2, 3, 3, 4]

        # diff_arr = [1, 0, 0]
        # [1, 1, 2, 3, 7, 10]
        # now, the challenge is the no.of pairs to select is dynamic i.e., depending on the p parameter, how do we tackle this

        # okay I got an idea, what if we get the difference array of nums and sort that array also, let'd do this
        # ** No man **, I think you missed THE crucial part, an index or an element can be only used once in pairs, shit......

        # diff_arr = [0] * (n-1)

        # for i in range(n-1):
        #     diff_arr[i] = abs(nums[i] - nums[i+1])  
        
        # diff_arr.sort()

        # return max(diff_arr[:p])

        def countPairs(target):
            i = count = 0

            while i < n-1:
                if nums[i+1] - nums[i] <= target:
                    count += 1
                    i += 1
                
                i += 1

            return count

        
        left, right = 0, nums[-1] - nums[0]

        while left <= right:
            mid = left + ((right - left) >> 1)

            if countPairs(mid) >= p:
                right = mid - 1
            else:
                left = mid + 1
            
        return left


# TC : O(n log nv) = O(n  log n + n log v)
# SC: O(n)
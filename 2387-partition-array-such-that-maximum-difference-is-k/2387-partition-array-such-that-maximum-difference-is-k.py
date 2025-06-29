class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # nums: int[]
        # k: int
        # nums.sort()

        # cur = nums[0]

        # partitions = 1

        # Greedy Approach   
        # example walk through
        # [3, 5, 8, 1, 2, 4, 9], k = 2

        # [1, 2, 3] [5, 4], [8, 9] # optimal
        # [1, 2] [3, 5, 4] [8, 9] # optimal
        # [1] [2, 3, 4] [5] [8, 9] # worst

        # [1, 2, 3, 4, 5, 8, 9]

        # min = 1

        # partitions = 1

        # cur - min > k # violating condition

        # 2 - 1 > 2 # no

        # 3 - 1 > 2 # no
        # 4 - 1 = 3 > 2 # yes, it is greater than 2

        # partitions += 1
        # min = 4

        # with the TC: O(n logn + n) => O(n log n)

        # SC: Python, tim-sort, which has the worst sc of O(n)



        # for num in nums:
        #     if num - cur > k:
        #         partitions += 1
        #         cur = num



        # Approach 2: Counting Sort -> Slightly Optimal

        n = len(nums)

        max_ele = max(nums)
        freq = [0] * (max_ele + 1)

        for num in nums:
            freq[num] += 1
        

        idx = partitions = 0

        while idx <= max_ele:
            while idx <= max_ele and freq[idx] == 0:
                idx += 1
            
            if idx > max_ele:
                break
            
            partitions += 1
            idx += k + 1
        
        return partitions




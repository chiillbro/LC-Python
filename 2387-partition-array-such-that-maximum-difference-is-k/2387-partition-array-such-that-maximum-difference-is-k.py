class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # nums: int[]
        # k: int
        nums.sort()

        cur = nums[0]

        partitions = 1

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



        for num in nums:
            if num - cur > k:
                partitions += 1
                cur = num
        
        return partitions




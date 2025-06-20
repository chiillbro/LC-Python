class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # nums: int[]
        # k: int
        nums.sort()

        cur = nums[0]

        partitions = 1

        for num in nums:
            if num - cur > k:
                partitions += 1
                cur = num
        
        return partitions




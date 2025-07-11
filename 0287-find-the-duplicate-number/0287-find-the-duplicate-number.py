class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]

        while True:
            # if not (hare < len(nums) and nums[hare] < len(nums)):
            #     return -1

            tortoise = nums[tortoise]

            hare = nums[nums[hare]]

            if tortoise == hare:
                break
        
        p1 = nums[0]
        p2 = tortoise

        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        
        return p1
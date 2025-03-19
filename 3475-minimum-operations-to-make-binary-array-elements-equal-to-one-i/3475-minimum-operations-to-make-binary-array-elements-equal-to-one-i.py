class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0

        # for i in range(2, len(nums)):
        #     if not nums[i-2]:
        #         count += 1
        #         nums[i-2] ^= 1
        #         nums[i-1] ^= 1
        #         nums[i] ^= 1

        # return count if sum(nums) == len(nums) else -1

        # ** Second Approach: Using Deque by tracking flips **

        flip_queue = deque()

        for i in range(len(nums)):
            while flip_queue and i > flip_queue[0] + 2:
                flip_queue.popleft()
            
            if (nums[i] + len(flip_queue)) % 2 == 0:
                if i + 2 >= len(nums):
                    return -1
                count += 1
                flip_queue.append(i)
        
        return count
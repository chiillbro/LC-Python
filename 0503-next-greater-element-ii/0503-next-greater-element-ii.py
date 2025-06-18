class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        stack = []

        res = [-1] * n

        for i in range(n * 2, -1, -1):
            index = i % n

            while stack and stack[-1] <= nums[index]:
                stack.pop()
            
            if stack:
                res[index] = stack[-1]
            
            stack.append(nums[index])

        return res
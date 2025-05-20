class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # nums = int[n]
        # queries = int[int[]] -> queries[i] = [li, ri]

        # Thought Process
        # I think it is the most brute force approach for this problem
        # 1. first thing is, we need to find how many times a particular index can be found from the queries array ranges
        # 2. now, map through the nums and see if the counts we calculated for the indices and the actual values here can be evaluated to zero or less

        # might give TLE
        n = len(nums)
        # freq = [0] * n

        # for l, r in queries:
        #     for i in range(l, r + 1):
        #         freq[i] += 1
        
        # for i, num in enumerate(nums):
        #     if num > freq[i]:
        #         return False
        
        # return True

        # I know, we somehow should make use of prefix sum, now let's think
        # and difference array
        # prefix = [0] * n
        # prefix[0] = nums[0]

        diff = [0] * (n+1)
        # diff[0] = nums[0]

        # for i in range(1, n):
        #     prefix[i] = prefix[i-1] + nums[i]
        #     diff[i] = nums[i] - nums[i-1]
        
        for l, r in queries:
            diff[l] += 1
            diff[r+1] -= 1
        
        operationCounts = [0] * n
        operationCounts[0] = diff[0]

        for i in range(1, n):
            operationCounts[i] = operationCounts[i-1] + diff[i]
        
        for operations, num in zip(operationCounts, nums):
            if operations < num:
                return False
        
        return True
        
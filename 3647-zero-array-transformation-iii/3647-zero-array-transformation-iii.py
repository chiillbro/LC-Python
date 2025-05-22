class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # queries.sort(key=lambda x: (x[0], -x[1]))
        # n = len(nums)

        # def can_transform(diff):
        #     i = 0
        #     cur = diff[0]
        #     while i < n:
        #         if cur < nums[i]:
        #             return False
        #         i += 1
        #         cur += diff[i]
            
        #     return True

        # diff = [0] * (n+1)

        # for i, (l, r) in enumerate(queries):
        #     diff[l] += 1
        #     diff[r+1] -= 1
        #     if can_transform(diff):
        #         return len(queries) - 1 - i
        
        # return -1 if not can_transform(diff) else 0

        n = len(nums)
        queries.sort()
        heap = []

        diff = [0] * (n+1)

        operations = 0
        j = 0

        for i, num in enumerate(nums):
            operations += diff[i]
            
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1
            
            while operations < num and heap and -heap[0] >= i:
                operations += 1
                diff[-heappop(heap)+1] -= 1
            
            if operations < num:
                return -1
        
        return len(heap)

            

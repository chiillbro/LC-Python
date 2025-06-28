class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # nums: int[]
        # k: int
        n = len(nums)

        # Sorting, TC: O(n log n)

        # sorted_nums = sorted(nums)

        # can do slight optimization using max heap
        # Priority Queue, TC: O(n log k)

        import heapq
        heap = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        indices = sorted([idx for _, idx in heap])

        return [nums[i] for i in indices]

        # return sorted_nums[n-k:]
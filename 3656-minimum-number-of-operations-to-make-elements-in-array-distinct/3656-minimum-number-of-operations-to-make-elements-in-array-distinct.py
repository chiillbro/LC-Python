class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = {}

        max_duplicate_idx = -1
        for i, num in enumerate(nums):
            if num in seen:
                max_duplicate_idx = max(seen[num], max_duplicate_idx)
            
            seen[num] = i
        
        return 0 if max_duplicate_idx == -1 else math.ceil((max_duplicate_idx + 1) / 3)
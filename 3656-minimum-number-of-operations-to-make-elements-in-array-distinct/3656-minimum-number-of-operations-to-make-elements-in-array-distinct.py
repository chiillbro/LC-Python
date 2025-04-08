class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = defaultdict(int)

        max_duplicate_idx = -1
        for i in range(len(nums)):
            if nums[i] in count:
                max_duplicate_idx = max(count[nums[i]], max_duplicate_idx)
            
            count[nums[i]] = i
        
        return 0 if max_duplicate_idx == -1 else math.ceil((max_duplicate_idx + 1) / 3)
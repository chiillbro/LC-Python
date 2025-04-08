class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = defaultdict(int)

        last = -1
        for i in range(len(nums)):
            if nums[i] in count and count[nums[i]] > last:
                last = count[nums[i]]
            
            count[nums[i]] = i
        
        return 0 if last == -1 else math.ceil((last + 1) / 3)
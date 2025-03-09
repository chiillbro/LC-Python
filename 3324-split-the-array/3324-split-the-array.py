class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        count_map = Counter(nums)
        
        return not any(v > 2 for v in count_map.values())
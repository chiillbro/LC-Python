class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        count_map = defaultdict(int)

        for num in nums:
            count_map[num] += 1
        
        return all(v <= 2 for v in count_map.values())
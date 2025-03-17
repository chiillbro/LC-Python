class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        N = len(nums)
        
        freq = Counter(nums)

        return all(not (count & 1) for count in freq.values())


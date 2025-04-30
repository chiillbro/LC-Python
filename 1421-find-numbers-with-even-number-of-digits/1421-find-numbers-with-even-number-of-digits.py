class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(0 if len(str(num)) & 1 else 1 for num in nums)
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)

        highest = max(freq.values())

        total = 0

        for val in freq.values():
            if val == highest:
                total += highest

        return total
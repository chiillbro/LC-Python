class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        ones = s.count("1")

        return s[:ones] == "1" * ones

class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1

        while i >= 0 and not (int(num[i]) & 1):
            i -= 1

        return num[:i + 1] if i >= 0 else ""
        
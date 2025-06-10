class Solution:
    def maxDifference(self, s: str) -> int:
        # s: string, consists of lowercase English Letters
        counts = Counter(s)

        return max(x for x in counts.values() if (x & 1)) - min(x for x in counts.values() if not (x & 1))
class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        i = 0

        changes = 0
        # while i < n-1:
        #     if s[i] != s[i+1]:
        #         changes += 1
        #     i += 2

        for i in range(0, n, 2):
            if s[i] != s[i+1]:
                changes += 1


        return changes

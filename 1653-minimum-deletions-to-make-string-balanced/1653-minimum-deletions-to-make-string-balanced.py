class Solution:
    def minimumDeletions(self, s: str) -> int:

        n = len(s)

        find_a = [0] * (n)

        for i in range(n-2, -1, -1):
            find_a[i] += find_a[i + 1]
            if s[i+1] == "a":
                find_a[i] += 1

        find_b = [0] * (n)

        for i in range(1, n):
            find_b[i] += find_b[i-1]
            if s[i-1] == "b":
                find_b[i] += 1
        
        min_deletions = n

        for i in range(n):
            prev_b_cnt = find_b[i]
            after_a_cnt = find_a[i]

            min_deletions = min(min_deletions, prev_b_cnt + after_a_cnt)
        
        return min_deletions

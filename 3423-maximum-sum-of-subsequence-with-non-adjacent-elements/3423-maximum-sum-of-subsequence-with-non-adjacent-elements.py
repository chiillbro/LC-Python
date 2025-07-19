class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = 1 << (n.bit_length())
        nums += [0] * (m - n)
        n = m
        tree = [[0] * 4 for _ in range(2 * n + 1)]

        def update(i, x):
            j = i + n
            tree[j][0] = max(0, x)
            while j:
                j >>= 1
                l0h0A, l1h0A, l0h1A, l1h1A = tree[2 * j]
                l0h0B, l1h0B, l0h1B, l1h1B = tree[2 * j + 1]
                # lo to hi
                tree[j][0] = max(l0h1A + l1h0B, l0h0A + l1h0B, l0h1A + l0h0B)
                # lo + 1 to hi
                tree[j][1] = max(l1h1A + l1h0B, l1h0A + l1h0B, l1h1A + l0h0B)
                # lo to hi - 1
                tree[j][2] = max(l0h1A + l1h1B, l0h0A + l1h1B, l0h1A + l0h1B)
                # lo + 1 to hi - 1
                tree[j][3] = max(l1h1A + l1h1B, l1h0A + l1h1B, l1h1A + l0h1B)

        for i, x in enumerate(nums):
            update(i, x)

        ans = 0
        for i, x in queries:
            update(i, x)
            ans += max(tree[1])
        return ans % 1_000_000_007
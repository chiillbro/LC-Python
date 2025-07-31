# class Solution:
#     def subarrayBitwiseORs(self, arr: List[int]) -> int:
#         n = len(arr)

#         dp = [[0] * (n) for _ in range(n)]

#         for sub_len in range(1, n+1):
#             for i in range(n - sub_len + 1):
#                 j = i + sub_len - 1

#                 dp[i][j] = -math.inf

#                 for k in range(i, j):



#         return dp[0][n-1]


class Solution(object):
    def subarrayBitwiseORs(self, A):
        ans = set()
        cur = {0}
        for x in A:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        steps = len(cost)

        # dp = [0] * (steps + 1)

        # dp[0] = 0
        # dp[1] = 0

        first, second = 0, 0

        for i in range(2, steps + 1):
            # dp[i] = min(
            #     dp[i-1] + cost[i-1],
            #     dp[i-2] + cost[i-2]
            # )
            cur = min(
                second + cost[i-1],
                first + cost[i-2]
            )
            second, first = cur, second


        # return dp[steps]
        return second
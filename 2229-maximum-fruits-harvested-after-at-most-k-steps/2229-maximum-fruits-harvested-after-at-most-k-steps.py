class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)

        pref_sums = [0] * (n + 1)
        indices = [0] * n

        for i in range(n):
            pref_sums[i+1] = pref_sums[i] + fruits[i][1]
            indices[i] = fruits[i][0]
        

        max_harvest = 0

        for x in range(k//2 + 1):
            y = k - 2*x

            left = startPos - x
            right = startPos + y

            start = bisect_left(indices, left)
            end = bisect_right(indices, right)

            max_harvest = max(max_harvest, pref_sums[end] - pref_sums[start])


            left = startPos - y
            right = startPos + x

            start = bisect_left(indices, left)
            end = bisect_right(indices, right)

            max_harvest = max(max_harvest, pref_sums[end] - pref_sums[start])

            max_harvest = max(max_harvest, pref_sums[end] - pref_sums[start])
        

        return max_harvest
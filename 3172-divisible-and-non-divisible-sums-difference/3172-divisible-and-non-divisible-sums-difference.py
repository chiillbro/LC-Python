class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # return sum(num if num % m else -num for num in range(1, n+1))

        # Approach two: Math

        k = n // m

        return (n * (n + 1) >> 1) - k * (k + 1) * m
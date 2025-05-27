class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # return sum(num if num % m else -num for num in range(1, n+1))

        # Approach two: Math

        # sum of numbers that are divisible by m, num2 = 1m + 2m + 3m + 4m + .... + km
        # where k = n//m, the maximum number of times within the range n
        # simplified = (1 + 2 + 3 + 4 + ... + k)m
        # (k(k+1) // 2)m
        # num1 = total_sum - num2 (divisible nums sum)
        # num1 - num2 = (n(n+1) // 2) - (k * (k+1) * m)

        k = n // m

        return (n * (n + 1) >> 1) - k * (k + 1) * m
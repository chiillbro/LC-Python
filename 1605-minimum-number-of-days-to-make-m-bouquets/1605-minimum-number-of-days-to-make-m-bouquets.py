class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        N = len(bloomDay)
        if m * k > N: return -1
        if m * k == 1: return min(bloomDay)
        low, high = min(bloomDay), max(bloomDay)

        def canForm(d):
            count = 0
            i = 0
            while i < N:
                j = i
                while j < N and bloomDay[j] <= d:
                    j += 1
                count += (j - i) // k
                while j < N and bloomDay[j] > d:
                    j += 1
                i = j
            return count >= m
        
        while low <= high:
            mid = low + (high - low) // 2
            if canForm(mid): high = mid - 1
            else: low = mid + 1
        
        return low

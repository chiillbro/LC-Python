class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        N = len(weights)

        low, high = max(weights), sum(weights)

        def canShip(w):
            curSum = 0
            count = 0
            for i in range(N):
                curSum += weights[i]
                if curSum > w:
                    count += 1
                    curSum = weights[i]
            
            if curSum <= w:
                count += 1
            return count

        while low <= high:
            mid = low + ((high - low) >> 1)
            cur = canShip(mid)
            if cur <= days:
                high = mid - 1
            else:
                low = mid + 1
        
        return low

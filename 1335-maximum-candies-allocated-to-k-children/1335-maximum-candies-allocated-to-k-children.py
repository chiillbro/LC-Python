class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        N = len(candies)
        low, high = 1, max(candies)

        def canDivideCandies(n):
            count = 0
            
            for candy in candies:
                count += (candy // n)
            return count >= k

        while low <= high:
            mid = low + ((high - low) >> 1)

            if canDivideCandies(mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return high
            
        


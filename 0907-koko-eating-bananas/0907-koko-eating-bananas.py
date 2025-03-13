class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        def canEat(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            return hours <= h

        while low <= high:
            mid = low + (high - low) // 2

            if canEat(mid): high = mid - 1
            else: low = mid + 1
        
        return low
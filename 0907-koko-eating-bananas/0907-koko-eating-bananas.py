class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h
        l, r = 1, max(piles)
        while l <= r:
            mid = l + (r-l) // 2
            if can_finish(mid): r = mid - 1
            else: l = mid + 1
        return l
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        N = len(ranks)
        maxRank = max(ranks)
        freq = [0] * (maxRank + 1)
        for rank in ranks:
            freq[rank] += 1

        def canRepair(time):
            cars_repaired = 0
            
            for rank in range(1, maxRank + 1):
                cars_repaired += freq[rank] * int(math.sqrt(time // rank))
            
            return cars_repaired >= cars

        low, high = 1, min(ranks) * (cars * cars)
        while low <= high:
            mid = (high + low) >> 1

            if canRepair(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low
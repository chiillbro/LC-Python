class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        N = len(ranks)
        maxRank = max(ranks)

        # ranks.sort()
        # This is a brilliant approach to create freq array to use ranks in sorted fashion without actually sorting(TC O(n logn)) it
        freq = [0] * (maxRank + 1)
        for rank in ranks:
            freq[rank] += 1

        def canRepair(time):
            cars_repaired = 0
            
            for rank in range(1, maxRank + 1):
                if freq[rank]:
                    cars_repaired += freq[rank] * int((time // rank) ** 0.5)
            # for rank in ranks:
            #     cars_repaired += int((time // rank) ** 0.5)
            
            return cars_repaired >= cars

        low, high = 1, min(ranks) * (cars * cars)
        # low, high = 1, cars * cars * ranks[0]

        while low <= high:
            mid = (high + low) >> 1

            if canRepair(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low
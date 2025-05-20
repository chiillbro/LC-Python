class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # nums = int[]

        counts = Counter(nums)

        uniques = sorted(counts.keys())
        
        prev = None
        skip = take = 0

        for num in uniques:
            max_points_so_far = max(skip, take)
            if prev == num - 1:
                take = num * counts[num] + skip
                skip = max_points_so_far
            else:
                take = num * counts[num] + max_points_so_far
                skip = max_points_so_far
            
            prev = num
        
        return max(take, skip)




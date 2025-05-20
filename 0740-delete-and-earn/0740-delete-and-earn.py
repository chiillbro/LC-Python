class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # nums = int[]

        counts = Counter(nums)

        uniques = sorted(counts.keys())
        
        prev = None
        skip = take = 0

        for num in uniques:
            max_points_up_to_prev = max(skip, take) # The best we could have done up to the prev block was max(skip, take)
            if prev == num - 1: # This means, num is an immediate neighbor of prev, if we take num, we could not have taken prev
                take = num * counts[num] + skip # new take would be the current block points num * counts[num] + the points we got by skipping prev which would be skip
                skip = max_points_up_to_prev # now new skip would be what if I have skipped this particular block, then I would have gotten the max_points before this block that is max_points_up_to_prev
            else:
                take = num * counts[num] + max_points_up_to_prev # skip the 
                skip = max_points_up_to_prev # If I skip the current block, my score is just whatever best score I had before the block which is max_points_up_to_prev
            
            prev = num
        
        return max(take, skip)




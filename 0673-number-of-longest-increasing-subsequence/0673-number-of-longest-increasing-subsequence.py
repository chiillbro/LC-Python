class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # IS = Increasing Subsequence
        # Initialization - each element itself is an LIS of length 1, and there's 1 ways to form it.
        lengths = [1] * n # the max height of an IS ending with nums[i]
        counts = [1] * n # how many ways to achieve that specific height ending with nums[i]

        # Let's assume we are building a tower with LEGOs
        for i in range(n):
            for j in range(i):
                # condition 1 -> Can nums[i] even go on top of nums[j]
                # if not, nums[j] i useless for building a tower that ends with nums[i], so we ignore it
                if nums[j] < nums[i]:
                    # here we have two scenarios
                    # 1. we found a NEW, TALLER way to build a tower ending at nums[i]
                    # This happens if lengths[j] + 1 > lengths[i]
                        # Update lengths[i]: The new record height for a tower ending at nums[i] is lengths[j] + 1
                        # Update counts[i]: How many ways to build this new tallest tower? It's exactly the no.of ways we could build the tower up to nums[j]. So, counts[i] = counts[j]. We're starting fresh with counting for this new height at i
                    # 2. We found another way to build a tower ending at nums[i] that's the SAME HEIGHT as the current tallest we know for nums[i]
                    # This happens if lengths[j] + 1 == lengths[i]
                        # lengths[i] does NOT change (it's already the max height)
                        # Update counts[i]: We add the no.of ways we could build the tower up to nums[j]. So, counts[i] += counts[j]. We found additional ways to achieve this existing max height for nums[i]
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
                
        max_length = max(lengths)
        return sum(counts[i] for i in range(n) if lengths[i] == max_length)


# The above solution runs in O(N^2) and is the standard dynamic programming aproach and is generally what's taught first.
# Still, there are more complex O(N log N) solutions involving data structures like Fenwick trees or segment trees, combined with coordinate compression and the O(N log N) LIS length algorithm idea. These are much harder to implement correctly, especially under the interview pressure.

# Note: the O(N^2) solution is very often the expected solution. It demonstrates good understanding of DP
# IF you implement the above solution clearly and explain it well, that's usually a strong pass for this problem


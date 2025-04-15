class FenwickTree:
    def __init__(self, size: int) -> None:
        self.tree = [0] * (size + 1)
    

    def update(self, index: int, delta: int) -> None:
        index += 1 # convert to 1-based index 

        while index <= len(self.tree) - 1:
            self.tree[index] += delta

            # index & -index -> gives the rightmost set bit
            # for ex: 6 & -6, 110 & 010 = 010 == 2 (second bit set)
            index += index & -index # Move to next index to update that covers the current index's range.
    
    def query(self, index: int) -> None:
        index += 1 # convert to 1-based index
        res = 0

        while index > 0:
            res += self.tree[index]
            index -= index & -index # jump to the parent block
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        # ** Approach : Binary Indexed Tree (BIT) : TC: O(n * log n), SC: O(n) **
        n = len(nums1)

        pos2 = [0] * n # pos2[val] = index of val in nums2
        reversedIdxMapping = [0] * n # corresponding index in nums1 for val in nums2
        for i, num2 in enumerate(nums2):
            pos2[num2] = i
        
        for i, num1 in enumerate(nums1):
            reversedIdxMapping[pos2[num1]] = i
        
        tree = FenwickTree(n)
        res = 0

        for value in range(n):
            pos = reversedIdxMapping[value]
            left = tree.query(pos)
            tree.update(pos, 1)
            right = (n - 1 - pos) - (value - left)

            res += left * right
        
        return res

# Summary
# Approach:
# The BIT technique here allows counting of valid left and right candidates for each position, effectively counting good triplets in O(nlogn).

# When to Use:
# Use this approach when the problem requires counting subsequences (or triplets) with ordering constraints and when you need efficient prefix queries.

# Mastery Tips:

# Ensure you’re comfortable with BIT operations (update, query).

# Practice mapping indices between two permutations.

# Work through small examples manually to see how BIT queries translate to valid counts.

# Use the cheat-sheet above as a checklist for similar problems.



# In BIT Update (index += index & -index):
# Every time you update the BIT (for example, when adding a value to an element), you need to update all subsequent blocks that include that element. The loop uses this operation to move from an index to all the indices that cover ranges including that index.

# In BIT Query (index -= index & -index):
# To query a prefix sum, you accumulate values from various blocks by moving backward from the given index until you reach 0. Each subtraction jumps you back by the size of the block that the current index covers.


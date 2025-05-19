class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # n pairs, 
        # pairs[i] = [lefti, righti] and lefti < righti
        # a pair [c, d] follows a pair [a, b] if b < c
        # return the longest chain, no order ristriction

        # Intuition ->
        # Sort the array based on second element
        pairs.sort(key=lambda x: (x[1], x[0]))
        cur_right = float("-inf"); count = 0

        for left, right in pairs:
            if left > cur_right:
                count += 1
                cur_right = right
        
        return count
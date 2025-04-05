from functools import reduce
import operator

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        # ** Approach one: Using backtracking to generate all subsets and for every subset, calcualte XOR and add it to the answer ** #
        # ** TC, SC : O(N * 2 ^ N) **

        # ans = 0
        # def backtrack(i: int, path: List[int]) -> None:
        #     nonlocal ans
        #     if i == n:
        #         subset_XOR_total = 0
        #         for num in path:
        #             subset_XOR_total ^= num
                
        #         ans += subset_XOR_total
        #         return
            
        #     backtrack(i + 1, path)
        #     path.append(nums[i])
        #     backtrack(i + 1, path)
        #     path.pop()
        
        # backtrack(0, [])
        # return ans


        # ** Approach 2: Now, we do something like optimized Bactracking by calculating the XOR while generating the subsets and passing current xor for that subset as an parameter ** #
        # ** TC : O(2 ^ N), SC: O(N) ** which is acceptable if N is small, as it usually for this problem **

        # def optimized_backtrack(i: int, xor: int) -> int:
        #     if i == n:
        #         return xor
            
        #     without_cur = optimizedBacktrack(i + 1, xor)

        #     with_cur = optimizedBacktrack(i + 1, xor ^ nums[i])

        #     return without_cur + with_cur

        # return optimizedBacktrack(0, 0)


        # ** Approach 3: Mathematical - useful for larger n **
        # TC: O(N), SC: O(1)

        # It can be proven that sum of the XOR of all th subsets is

        # = 2^(n-1) * (bitwise OR of all elements in the nums)

        return (1 << (n - 1)) * reduce(operator.or_, nums, 0)

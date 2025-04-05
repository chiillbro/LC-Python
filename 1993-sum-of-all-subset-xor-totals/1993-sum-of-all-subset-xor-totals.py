class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        def backtrack(i: int, path: List[int]) -> None:
            nonlocal ans
            if i == n:
                subset_XOR_total = 0
                for num in path:
                    subset_XOR_total ^= num
                
                ans += subset_XOR_total
                return
            
            backtrack(i + 1, path)
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
        
        backtrack(0, [])
        return ans
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0

        def backtrack(cur: int, path: List[int]) -> None:
            nonlocal ans
            if cur == n:
                xor = 0
                for num in path:
                    xor ^= num
                
                ans += xor
                return
            
            backtrack(cur + 1, path)
            path.append(nums[cur])
            backtrack(cur + 1, path)
            path.pop()
        
        backtrack(0, [])
        return ans
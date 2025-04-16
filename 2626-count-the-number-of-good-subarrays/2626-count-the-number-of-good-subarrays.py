class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        # Two Pointers (Dynamic Sliding Window) TC: O(n), SC: O(n)
        n = len(nums)
        look_up = defaultdict(int)

        cur_count, r = 0, -1
        res = 0
        for l in range(n):
            while cur_count < k and r + 1 < n:
                r += 1
                cur_count += look_up[nums[r]]
                look_up[nums[r]] += 1
            
            if cur_count >= k:
                res += n - r
            look_up[nums[l]] -= 1
            cur_count -= look_up[nums[l]]
        
        return res


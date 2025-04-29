class Solution:
    def sliding_window_at_most(self, nums: List[int], k: int) -> int:
        n = len(nums)

        freq_map = defaultdict(int)
        left = res = 0

        for right in range(n):
            freq_map[nums[right]] += 1

            while left <= right and len(freq_map) > k:
                freq_map[nums[left]] -= 1
                if not freq_map[nums[left]]:
                    freq_map.pop(nums[left])
                
                left += 1
            
            res += right - left + 1
        
        return res

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.sliding_window_at_most(nums, k) - self.sliding_window_at_most(nums, k - 1)

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # using Sliding Window Approach

        n = len(nums)
        distinct = len(set(nums))

        freq_map = defaultdict(int)
        left = res = 0

        for right in range(n):
            freq_map[nums[right]] += 1

            while len(freq_map) == distinct:
                res += n - right
                freq_map[nums[left]] -= 1
                if not freq_map[nums[left]]:
                    freq_map.pop(nums[left])
                
                left += 1
        
        return res
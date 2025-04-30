class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_ele = max(nums)

        res = left = 0
        max_ele_count = 0

        for right in range(n):
            if nums[right] == max_ele:
                max_ele_count += 1
            
            # This loop runs AS LONG AS the window [left..right] is VALID (>= k max_ele's).
            # Crucially, it enters when max_ele_count *first* becomes k.
            while max_ele_count == k:   # Note: Using >= k is equivalent to == k here due to the shrinking logic
                 # --- CORE LOGIC ---
                # If the window nums[left..right] is valid (has >= k max_ele's),
                # then ANY subarray that starts at 'left' and ends at 'right' or later
                # MUST also be valid.
                # These subarrays are: nums[left..right], nums[left..right+1], ..., nums[left..n-1].
                # The number of such subarrays is (n-1) - right + 1 = n - right.
                # We add this count because we've found 'n - right' new valid subarrays
                # anchored by this 'left' position.
                res += n - right

                # Now, try to shrink the window from the left to find the *next possible*
                # minimal valid window ending later (or maybe make the current one invalid).
                if nums[left] == max_ele:
                    max_ele_count -= 1  # Decrement count as max_ele is leaving window
                
                left += 1   # Shrink window
        
        return res
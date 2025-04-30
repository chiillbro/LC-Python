class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        # Classic Counting Sub arrays with variblbe-size window **Sliding Window** Pattern #

        # Here is the standard template to solve these type of problems

        # ******************** Template Start ********************* #
        def variable_window_count_subarrays(arr, condition_func):
            n = len(arr)
            left = 0
            count = 0
            # window_state = ... # Initialize state (sum, freq_map, count, etc.)

            for right in range(n):
                # 1. Expand window: Update state with arr[right]
                # window_sum += arr[right]
                # freq_map[arr[right]] += 1

                # 2. Shrink window: While the window violates the condition...
                while not condition_func(window_state): # Or condition_is_violated(window_state)
                    # Remove arr[left]'s contribution from state
                    # window_sum -= arr[left]
                    # freq_map[arr[left]] -= 1
                    # if freq_map[arr[left]] == 0: del freq_map[arr[left]]
                    left += 1 # Move left pointer

                # 3. Update result: Now window [left..right] is valid.
                # ALL subarrays ending at 'right' and starting from 'left' onwards are valid.
                # These are: arr[left..right], arr[left+1..right], ..., arr[right..right]
                # There are (right - left + 1) such subarrays.
                count += (right - left + 1)

            return count

            # ******************** Template End ********************* #

            
        n = len(nums)

        res = 0
        left = 0
        _sum = 0
        for right in range(n):
            _sum += nums[right]

            while left <= right and _sum * (right - left + 1) >= k:
                _sum -= nums[left]
                left += 1
            
            res += (right - left + 1)
        
        return res
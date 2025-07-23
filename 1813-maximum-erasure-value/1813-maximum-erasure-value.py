class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # sliding window

        n = len(nums)

        # pref_sums = [0] * (n)

        # pref_sums[0] = nums[0]

        # for i in range(1, n):
        #     pref_sums[i] = pref_sums[i-1] + nums[i]

        # don't even need prefix sum array

        seen = set()

        left = 0
        cur_sum = 0
        max_sum = 0
        for right in range(n):
            while nums[right] in seen:
                cur_sum -= nums[left]
                seen.remove(nums[left])
                left += 1

            seen.add(nums[right])

            # cur_sum = pref_sums[right] - (pref_sums[left-1] if left > 0 else 0)
            cur_sum += nums[right]

            max_sum = max(max_sum, cur_sum)
    
        return max_sum
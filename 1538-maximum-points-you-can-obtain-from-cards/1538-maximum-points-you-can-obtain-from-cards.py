class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return sum(nums)

        # start = n - k
        # length = k << 1
        # left = 0
        # res = current_sum = 0

        # for right in range(length):
        #     current_sum += nums[(start + right) % n]

        #     if right - left + 1 > k:
        #         current_sum -= nums[(left + start) % n]
        #         left += 1

            # if right - left + 1 == k:
            #     res = max(res, current_sum)


        # More Straightforward Approach

        current_sum = sum(nums[:k])
        res = current_sum

        for i in range(k):
            current_sum -= nums[k - 1 - i] # remove the rightmost currently included element from the beginning
            current_sum += nums[n - 1 - i] # add the rightmost not yet included element from the end

            res = max(current_sum, res)
        
        return res

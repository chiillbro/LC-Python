class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        n = len(nums)

        sorted_nums = sorted(nums)

        dp = dict() # value -> the possible longest length of the consecutive group ending at this value

        for i in range(n):
            num = sorted_nums[i]

            dp[num+1] = dp.get(num, 0) + 1 # to avoid, duplicate or extra counting, let's first compute for the increased value of curr element
            dp[num] = dp.get(num-1, 0) + 1
        

        return max(dp.values())
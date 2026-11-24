class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)

        max_length = 0
        for i in range(n):
            for j in range(i+1, n):
                sub_array = nums[i:j+1]

                if math.prod(sub_array) == math.lcm(*sub_array) * math.gcd(*sub_array):
                    max_length = max(max_length, len(sub_array))
        

        return max_length
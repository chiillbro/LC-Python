class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)

        max_length = 0
        for i in range(n):
            run_prod = run_gcd = run_lcm = nums[i]
            for j in range(i+1, n):
                # sub_array = nums[i:j+1]

                # if math.prod(sub_array) == math.lcm(*sub_array) * math.gcd(*sub_array):
                #     max_length = max(max_length, len(sub_array))
                run_prod *= nums[j]
                run_gcd = math.gcd(run_gcd, nums[j])
                run_lcm = math.lcm(run_lcm, nums[j])

                if run_prod == run_gcd * run_lcm:
                    max_length = max(max_length, j-i+1)
        

        return max_length
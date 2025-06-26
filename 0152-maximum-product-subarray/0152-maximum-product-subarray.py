class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kandane's Algo (Dynamic Programming Approach)

        # res = min_so_far = max_so_far = nums[0]

        # for num in nums[1:]:
        #     temp = min(num, min_so_far * num, max_so_far * num)
        #     max_so_far = max(num, min_so_far * num, max_so_far * num)

        #     min_so_far = temp

        #     res = max(res, max_so_far)
        
        # return res


        # More Intuitve

        n = len(nums)
        max_product = -math.inf
        
        left_product = right_product = 1

        for left in range(n):
            right = n - left - 1

            left_product *= nums[left]
            right_product *= nums[right]

            max_product = max(max_product, left_product, right_product)

            if left_product == 0:
                left_product = 1
            
            if right_product == 0:
                right_product = 1
        
        return max_product

            
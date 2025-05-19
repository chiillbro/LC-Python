class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # counter = Counter(nums)
        _sum = sum(nums)

        if nums.count(_sum // 3) == 3: return "equilateral"

        for num in nums:
            if not (_sum - num > num):
                return "none"
        if nums.count(nums[0]) == 2 or nums.count(nums[1]) == 2:
            return "isosceles"
        
        return "scalene"

        # if len(counter) == 2: return "isosceles"

        # if len(counter) == 3: return "scalene"

        # return "none"
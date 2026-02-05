class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                idx = (num + i) % n

                res.append(nums[idx])
            
            elif num < 0:
                idx = abs(num)
                if idx > i:
                    idx -= i
                    idx %= n
                    res.append(nums[-(idx)])
                else:
                    res.append(nums[-(n - i + idx)])
            
            else:
                res.append(num)

            

        return res
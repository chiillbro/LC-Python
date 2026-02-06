class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)


        return [nums[((i + v) % n)] for i, v in enumerate(nums)]
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                idx = (num + i) % n
                res.append(nums[idx])
            
            elif num < 0:
                idx = (n - i + abs(num)) % n
                res.append(nums[-idx])
                # idx = abs(num)
                # if idx > i:
                #     idx -= i
                #     idx %= n
                #     res.append(nums[-(idx)])
                # else:
                #     res.append(nums[-(n - i + idx)])
            
            else:
                res.append(num)

            

        return res
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # In any given array, only two elements can exist with the frequency n // 3

        n = len(nums)

        k = n // 3

        candidate1 = candidate2 = None
        cnt1 = cnt2 = 0

        for num in nums:
            if num == candidate1:
                cnt1 += 1
            elif num == candidate2:
                cnt2 += 1
            elif cnt1 == 0:
                candidate1 = num
                cnt1 = 1
            elif cnt2 == 0:
                candidate2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1 = cnt2 = 0

        for num in nums:
            if num == candidate1:
                cnt1 += 1
        
            if num == candidate2:
                cnt2 += 1
        
        res = []
        if cnt1 > k:
            res.append(candidate1)

        if cnt2 > k and candidate2 != candidate1:
            res.append(candidate2)
        
        return res
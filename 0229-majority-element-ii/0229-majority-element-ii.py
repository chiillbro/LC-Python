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

        n = len(nums) // 3
        # count = Counter(nums)
        # return [k for k, v in count.items() if v > n]

        # Follow-Up Optimal Solution using Boyer-Moore Majority Voting Algorithm
        c1 = c2 = None
        count1 = count2 = 0

        for num in nums:
            if num == c1:
                count1 += 1
            elif num == c2:
                count2 += 1
            elif count1 == 0:
                c1 = num
                count1 = 1
            elif count2 == 0:
                c2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0

        for num in nums:
            if num == c1:
                count1 += 1
            
            if num == c2:
                count2 += 1
        
        res = []
        if count1 > n:
            res.append(c1)
        
        if count2 > n and c2 != c1:
            res.append(c2)
        
        return res
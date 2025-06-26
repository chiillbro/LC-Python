class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

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

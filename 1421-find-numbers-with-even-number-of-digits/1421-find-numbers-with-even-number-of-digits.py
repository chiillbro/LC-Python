class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Approach 1: By extracting digits, TC: O(N * log M)

        # count = 0
        # for num in nums:
        #     digits = 0
        #     while num:
        #         digits += 1
        #         num //= 10
            
        #     if not digits & 1:
        #         count += 1
        
        # return count


        # Approach 2: Converting to string, TC: O(N * log M)

        # return sum(0 if len(str(num)) & 1 else 1 for num in nums)



        # Approach 3: Using logarithmic expression, TC: O(N * log M)
        
        # return sum(1 if not (int(math.floor(math.log10(num)))) + 1) & 1 else 0 for num in nums




        # Approach 4: Look At constraints -> Clever Method: TC O(N)

        count = 0

        for num in nums:
            if 10 <= num <= 99 or 1000 <= num <= 9999 or num == 100000:
                count += 1
        
        return count


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # Direct, Initial thought Approach
        if n <= 0:
            return False

        # while not (n & 1):
        #     n //= 2
        
        # return n == 1


        # Intuition: 2's power numbers are special, they have only one bit set ('1'), so we can simply count the '1''s and check whether they are equal to 1
        # return bin(n).count('1') == 1


        # Bit Manipulation Trick using (AND operator)

        return n > 0 and (n & (n-1)) == 0
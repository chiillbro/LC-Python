class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # Direct, Initial thought Approach
        # if n <= 0:
        #     return False

        # while not (n & 1):
        #     n //= 2
        
        # return n == 1


        # Intuition: 2's power numbers are special, they have only one bit set ('1'), so we can simply count the '1''s and check whether they are equal to 1
        # return n > 0 and bin(n).count('1') == 1 # or,
        # return n > 0 and n.bit_count() == 1 # we can do something like,


        # Bit Manipulation Trick using (AND operator)

        # return n > 0 and (n & (n-1)) == 0



        # Logarithmic Approach

        if n <= 0:
            return False

        val = math.log2(n)
        print("val", val)

        return 2**round(val) == n
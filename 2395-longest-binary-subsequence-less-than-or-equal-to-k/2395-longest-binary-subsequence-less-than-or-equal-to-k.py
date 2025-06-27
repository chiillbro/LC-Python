class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        n = len(s)

        val = 0
        j = n-1
        # greedily compute the value based on 
        # the right most set bits and keeping the k constraint in mind
        while j >= 0:
            if s[j] == '1':
                set_bit = n - j -1
                val += 1 << set_bit
            
            if val > k:
                break
            j -= 1
        
        # if j becomes -1 which means,
        # all of the binary representation given can contribute to the LBS
        if j == -1 and val <= k:
            return n

        # as we need longest subsequence and problem states that subsequence can contain leading zeroes
        # count the number of zeroes that can contribute
        zeroes_till_j = 0

        for i in range(j):
            if s[i] == '0':
                zeroes_till_j += 1
        
        # while processing next left set bit from right, 
        # we might have crossed '0' 's just before val becomes > k
        # so traversing back j
        while j < n-1 and s[j+1] == '0':
            j += 1
            zeroes_till_j += 1

        # now, at this point of time j+1 holds the position where val >= k
        
        # n - j - 1 = length of satisfying k length and extra zeroes that can be appended left
        return n - j - 1 + zeroes_till_j


# ** Complexity Analysis **  #

# TC: Amortized O(N), we visit almost all positions at most once and every other arithmetic operations are O(1)

# SC: O(1), just a few variables, no extra space

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        str1 = "01"
        str2 = "10"

        if n & 1:
            str1 += str1 * ((n-3) >> 1) + "0"
            str2 += str2 * ((n-3) >> 1) + "1"
        
        else:
            str1 += str1 * ((n-2) >> 1)
            str2 += str2 * ((n-2) >> 1)
        
        ans1 = 0
        ans2 = 0

        for i in range(len(s)):
            a, b, c = s[i], str1[i], str2[i]

            if a != b:
                ans1 += 1
            
            if a != c:
                ans2 += 1
        

        return min(ans1, ans2)
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # str1 = "01"
        # str2 = "10"

        # if n & 1:
        #     str1 += str1 * ((n-3) >> 1) + "0"
        #     str2 += str2 * ((n-3) >> 1) + "1"
        
        # else:
        #     str1 += str1 * ((n-2) >> 1)
        #     str2 += str2 * ((n-2) >> 1)
        
        # ans1 = 0
        # ans2 = 0

        # for i in range(len(s)):
        #     a, b, c = s[i], str1[i], str2[i]

        #     if a != b:
        #         ans1 += 1
            
        #     if a != c:
        #         ans2 += 1
        

        # return min(ans1, ans2)


        start0 = 0
        start1 = 0


        for i in range(n):
            if i & 1:
                if s[i] == "0":
                    start1 += 1
                else:
                    start0 += 1
                
            else:
                if s[i] == "1":
                    start1 += 1
                else:
                    start0 += 1
        

        return min(start0, start1)



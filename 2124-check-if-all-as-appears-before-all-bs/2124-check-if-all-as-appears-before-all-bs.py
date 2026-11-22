class Solution:
    def checkString(self, s: str) -> bool:
        
        return "ba" not in s # there should be no "ba" if exists, then return False
    

        # ----------------------------
        # return list(s) == sorted(s)
        
        
        # -----------------------
        
        # return s == 'a'*s.count('a') + 'b'*s.count('b')
        
        # -------------------
        # b_count = s.count('b')

        # if b_count and s[-b_count:] != 'b' * b_count:
        #     return False
        
        # return True
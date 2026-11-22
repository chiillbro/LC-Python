class Solution:
    def checkString(self, s: str) -> bool:
        b_count = s.count('b')

        if b_count and s[-b_count:] != 'b' * b_count:
            return False
        
        return True
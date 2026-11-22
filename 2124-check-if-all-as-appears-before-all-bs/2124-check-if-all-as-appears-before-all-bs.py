class Solution:
    def checkString(self, s: str) -> bool:
        b_count = s.count('b')

        if not b_count:
            return True

        if s[-b_count:] != 'b' * b_count:
            return False
        
        return True
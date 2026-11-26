class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # dup_s = s
        
        def perform_round(x):
            new_str = ""
            for i in range(0, len(x), k):
                curr = sum(int(c) for c in s[i:i+k])
                
                new_str += str(curr)
            
            return new_str
                    
                
        while len(s) > k:
            s = perform_round(s)
        
        return s
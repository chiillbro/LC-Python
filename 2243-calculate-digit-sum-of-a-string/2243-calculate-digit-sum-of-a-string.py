class Solution:
    def digitSum(self, s: str, k: int) -> str:
        dup_s = s
        
        def perform_round(x):
            new_str = ""
            for i in range(0, len(x), k):
                curr = 0
                for j in range(i, min(i+k, len(x))):
                    curr += int(x[j])
                
                new_str += str(curr)
                
            
            return new_str
                    
                
        while len(dup_s) > k:
            dup_s = perform_round(dup_s)
        
        return dup_s
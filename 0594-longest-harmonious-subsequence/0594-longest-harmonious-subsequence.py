class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)

        res = 0
        for num in nums:
            max_freq = None
            if num + 1 in freq:
                max_freq = freq[num+1]
            
            if num - 1 in freq:
                max_freq = max(max_freq, freq[num-1]) if max_freq != None else freq[num-1]
            
            if max_freq:
                res = max(res, freq[num] + max_freq)
    
        return res
            


            

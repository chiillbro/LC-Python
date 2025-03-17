class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        my_dict = defaultdict(int)

        for char in s:
            my_dict[char] += 1
        
        for char in t:
            if my_dict[char] == 0:
                return False
            my_dict[char] -= 1
        
        return True
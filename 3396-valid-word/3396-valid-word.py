class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
            
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        vowel_seen = False
        consonant_seen = False
        for c in word:
            if not c.isalnum():
                return False
            
            if c in vowels:
                vowel_seen = True
            elif c.isalpha():
                consonant_seen = True
        
        return vowel_seen and consonant_seen
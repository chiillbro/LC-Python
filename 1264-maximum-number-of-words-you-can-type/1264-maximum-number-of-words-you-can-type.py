class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s = set(brokenLetters)

        words = text.split(" ")
        can_fully_type = len(words)

        for word in words:
            for c in word:
                if c in s:
                    can_fully_type -= 1
                    break
            
        
        return can_fully_type

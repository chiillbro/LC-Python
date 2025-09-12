class Solution:
    def sortVowels(self, s: str) -> str:
        s_list = list(s)

        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}

        vowels_in_s = [c for c in s_list if c in vowels]

        if not vowels_in_s:
            return s

        vowels_in_s.sort(key=lambda x: ord(x))
        j = 0
        for i, c in enumerate(s_list):
            if c in vowels:
                s_list[i] = vowels_in_s[j]
                j += 1
        
        return ''.join(s_list)
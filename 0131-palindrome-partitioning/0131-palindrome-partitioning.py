class Solution:
    def checkPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i <= j and s[i] == s[j]:
            i += 1
            j -= 1
        
        return i > j
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        def backtrack(i, partition):
            if i == n:
                res.append(partition[:])
                return
            for j in range(i, n):
                if self.checkPalindrome(s[i:j+1]):
                    partition.append(s[i:j+1])
                    backtrack(j + 1, partition)
                    partition.pop()
        
        backtrack(0, [])

        return res
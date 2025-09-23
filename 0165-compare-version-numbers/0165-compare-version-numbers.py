class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n1, n2 = len(version1), len(version2)

        i = j = 0
        while i < n1 or j < n2:
            revision1, revision2 = [], []
            while i < n1 and version1[i] != '.':
                revision1.append(version1[i])
                i += 1
            i += 1

            while j < n2 and version2[j] != '.':
                revision2.append(version2[j])
                j += 1
            j += 1

            digit1, digit2 = int(''.join(revision1)) if revision1 else 0, int(''.join(revision2)) if revision2 else 0
            if digit1 < digit2:
                return -1
            elif digit1 > digit2:
                return 1

        # while i < n1:
        #     revision1 = []
        #     while i < n1 and version1[i] != '.':
        #         revision1.append(version1[i])
        #         i += 1
        #     i += 1

        #     if int(''.join(revision1)) != 0:
        #         return 1
        
        return 0
            
        
        

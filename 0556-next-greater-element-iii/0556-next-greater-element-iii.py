class Solution:
    def nextGreaterElement(self, n: int) -> int:
        list_n = list(str(n))

        N = len(list_n)

        i = N - 2

        while i >= 0 and list_n[i] >= list_n[i+1]:
            i -= 1
        
        if i < 0:
            return -1

        j = N - 1

        while j >= 0 and list_n[j] <= list_n[i]:
            j -= 1

        list_n[i], list_n[j] = list_n[j], list_n[i]

        list_n[i+1:] = reversed(list_n[i+1:])

        res = int(''.join(list_n))

        if res >= (1 << 31):
            return -1
        
        return res
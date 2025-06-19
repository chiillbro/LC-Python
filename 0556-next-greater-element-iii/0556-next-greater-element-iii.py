class Solution:
    def nextGreaterElement(self, n: int) -> int:
        list_n = list(str(n))

        N = len(list_n)

        i = N - 2


        # find the first index where idx[i] < idx[i+1]
        while i >= 0 and list_n[i] >= list_n[i+1]:
            i -= 1
        
        # if there is no such index, then it's impossible to form a number that is greater
        if i < 0:
            return -1

        j = N - 1

        # Now we need to find an index from the end where idx[j] > idx[i]
        while j >= 0 and list_n[j] <= list_n[i]:
            j -= 1

        # swap the two elements
        list_n[i], list_n[j] = list_n[j], list_n[i]

        # Now, as we are asked to return the next greater element
        # We need to reverse the elements from i + 1 till end, as this will help us to get the nearest and just greater number to the given number
        list_n[i+1:] = reversed(list_n[i+1:])

        res = int(''.join(list_n))

        # as mentioned, if the found greater element doesn't fit 32 bit integer (2 ** 31 - 1), then we should return -1

        # can also check like thie, res.bit_length() <= 32:
        if res >= (1 << 31):
            return -1
        
        return res
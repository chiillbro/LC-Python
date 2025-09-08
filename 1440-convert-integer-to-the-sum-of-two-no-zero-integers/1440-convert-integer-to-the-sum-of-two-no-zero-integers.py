class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # no-zero integer is a positive integer that does not contain any 0 in its decimal representation
        a = 1
        while True:
            b = n - a

            if "0" not in str(a) and "0" not in str(b):
                return [a, b]
            
            a += 1
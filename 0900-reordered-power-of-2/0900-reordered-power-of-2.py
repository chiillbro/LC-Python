class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def convert(n):
            return ''.join(sorted(str(n)))
        
        target = convert(n)

        for i in range(31):
            if convert(1 << i) == target:
                return True
        
        return False


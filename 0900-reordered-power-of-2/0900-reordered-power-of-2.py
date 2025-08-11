class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # def convert(n):
        #     return ''.join(sorted(str(n)))
        
        # target = convert(n)

        # for i in range(31):
        #     if convert(1 << i) == target:
        #         return True
        
        # return False


        # Counting Approach

        counter1 = Counter(str(n))

        for i in range(31):
            counter2 = Counter(str(1 << i))

            if counter1 == counter2:
                return True
        
        return False


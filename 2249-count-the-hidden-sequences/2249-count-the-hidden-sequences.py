class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # num1 = next - prev
        # num2 = next2 - next

        # num1 - num2 = 2*next -next2 - prev

        # [3, 4, 1, 5]

        # num1 + num2 = next2 - prev


        # n = len(differences)
        # res = 0
        # for i in range(lower, upper + 1):
        #     elems = 1
        #     last = i
        #     for num in differences:
        #         nex = last + num

        #         if nex < lower or nex > upper:
        #             break
        #         last = nex
        #         elems += 1
        #     if elems == n + 1:
        #         res += 1
        
        # return res

        x = y = cur = 0

        for d in differences:
            cur += d
            x = min(x, cur)
            y = max(y, cur)
            if y - x > upper - lower:
                return 0
        
        return (upper - lower) - (y - x) + 1

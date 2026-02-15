# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         n, m = len(a), len(b)

#         if m > n:
#             return self.addBinary(b, a)


#         carry = 0

#         i = n - 1
#         j = m - 1
        
#         res = []
#         while i >= 0 and j >= 0:
#             # print(i, j, n, m)
#             u, v = a[i], b[j]
#             cur = 0
#             if (u == "1" and v == "1"):
#                 cur = 0
#                 carry = 1
#             elif u == "0" and v == "0":
#                 if carry:
#                     cur = 1
#                     carry = 0
#                 else:
#                     cur = 0
#             else:
#                 cur = 1
            
#             if cur == 0:
#                 res.append("0")
#             else:
#                 res.append("1")

#             # if cur or carry:
#             #     res.append("1")
#             #     carry = 0
#             # else:
#             #     res.append("0")


#             i -= 1
#             j -= 1

#         while i >= 0:
#             cur = a[i]

#             if cur == "0":
#                 if carry:
#                     res.append("1")
#                     carry = 0
#                 else:
#                     res.append(0)
#             else:
#                 if carry:
#                     res.append("0")
#                 else:
#                     res.append(cur)
            
#             i -= 1

        
#         if carry:
#             res.append("1")

#         res.reverse()

#         return "".join(res)




class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxL = max(len(a), len(b))
        C = 0
        res = []

        def sum_bit(A, B, C):
            return (A ^ B) ^ C

        def carry_bit(A, B, C):
            return (A & B) | ((A ^ B) & C)

        for i in range(maxL):
            A = int(a[-1 - i]) & 1 if i < len(a) else 0
            B = int(b[-1 - i]) & 1 if i < len(b) else 0

            res.append(str(sum_bit(A, B, C)))
            C = carry_bit(A, B, C)

        if C: res.append(str(C))

        return "".join(reversed(res))

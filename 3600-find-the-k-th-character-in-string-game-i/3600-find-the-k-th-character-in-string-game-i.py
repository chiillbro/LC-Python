class Solution:
    def kthCharacter(self, k: int) -> str:

        # Optimal Approch

        return chr(97 + (k-1).bit_count())

        # res = 0

        # while k != 1:
        #     t = k.bit_length() - 1
        #     if (1 << 1) == k:
        #         t -= 1
            
        #     k = k - (1 << t)

        #     res += 1
        
        # return chr(97 + res)
        # queue = deque(["a"])

        # count = 1

        # while count < k:
        #     for i in range(len(queue)):
        #         cur = queue[i]

        #         nxt = chr(ord(cur) + 1)

        #         queue.append(nxt)

        #         count += 1


        # return queue[k-1]
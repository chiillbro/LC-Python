class Solution:
    def kthCharacter(self, k: int) -> str:
        queue = deque(["a"])

        count = 1

        while count < k:
            print("queue", queue)
            for i in range(len(queue)):
                cur = queue[i]

                print("cur", cur)
                nxt = chr(ord(cur) + 1)

                print("nxt", nxt)

                queue.append(nxt)

                count += 1


        return queue[k-1]
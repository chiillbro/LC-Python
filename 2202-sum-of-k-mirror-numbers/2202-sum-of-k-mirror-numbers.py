class Solution:
    def kMirror(self, k: int, n: int) -> int:
        left, cnt, ans = 1, 0, 0

        while cnt < n:
            right = left * 10

            for parity in [0, 1]:
                for i in range(left, right):
                    if cnt == n:
                        return ans
                    
                    palindrome = i
                    x = i // 10 if not parity else i

                    while x:
                        palindrome = palindrome * 10 + x % 10
                        x //= 10

                    baseK = self.getBaseK(palindrome, k)

                    if baseK == baseK[::-1]:
                        cnt += 1
                        ans += palindrome
            
            left = right
        
        return ans
        
    
    def getBaseK(self, n, k):
        res = []

        while n:
            rem = n % k

            res.append(rem)

            n //= k

        # res.reverse()

        return res